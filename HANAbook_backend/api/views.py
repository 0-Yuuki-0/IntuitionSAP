from django.shortcuts import render
from api.models import *
from api.serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from datetime import datetime, timedelta
from rest_framework import permissions

# from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

'''
    Authentication APIs:
        POST - Login (JWT will be good)
        POST - Register
        POST/GET - Logout
    Clinics APIs:
        Dashboard data (vaccined today, total today appointments, total users,  total people vaccined in every month array )
        GET -  All Schedules
        GET - Single schedule detail
        PUT - Update schedule data
        DELETE - Schedule cancellation
        GET - Clinics: All Patients
        DELETE - Patients Delete
    User APIs:
        GET - Upcoming schedule
        GET - All schedules (for apptment history)
        GET - Make appointment data (available clinics, available appointment times)
        POST - Make an appointment
        POST - Check in
'''

# Create your views here.

CHECK_IN_TIME_LIMIT = 3


class ClinicListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ClinicSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs = Clinic.objects.all()

        # custom filters
        # username = self.request.query_params.get('username')
        # if username != None:
        #     qs = qs.filter(username=username)
        
        return qs

    def perform_create(self, serializer):
        serializer.save(is_clinic=True)
        

class PatientListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs = Patient.objects.all()

        if self.user.is_anonymous:
            return Response({'message': "Sign in to view Patients."}, status=status.HTTP_401_UNAUTHORIZED)

        # custom filters
        # username = self.request.query_params.get('username')
        # if username != None:
        #     qs = qs.filter(username=username)

        # filter by permissions
        user = self.request.user
        if user.is_patient:
            qs = qs.filter(id=user.id)
        
        return qs

    def perform_create(self, serializer):
        serializer.save(is_patient=True)


class AppointmentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Appointment.objects.all()

        # custom filters
        # username = self.request.query_params.get('username')
        # if username != None:
        #     qs = qs.filter(username=username)
        
        return qs
    
    def create(self, request, *args, **kwargs):
        user = request.user
        if user.is_patient:
            return Response({'message': "Patient cannot create Appoitnments."}, status=status.HTTP_401_UNAUTHORIZED)
        if user.is_clinic:
            clinic = Clinic.objects.get(id=user.id)
            request.data['clinic'] = clinic.name
        if request.data['date_time'] > datetime.datetime.now():
            return Response({'message': "Please set a time that hasn't passed yet."}, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AppointmentRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        restricted_attrs = ['clinic', 'date_time', 'doctor']
        user = request.user
        if user.is_patient:
            for attr in restricted_attrs:
                try:
                    attr = request.data['attr']
                    msg = "Patient cannot set %s attribute." % attr
                    return Response({'message':msg}, status=status.HTTP_400_BAD_REQUEST)
                except:
                    pass
            try:
                _ = request.data['patient']
                patient = Patient.objects.get(id=user.id)
                request.data['patient'] = patient.name
            except:
                pass

        time_to_appt = request.data['date_time'] - datetime.datetime.now()
        time_to_appt = time_to_appt.total_seconds() / (60 * 60)
        if time_to_appt > CHECK_IN_TIME_LIMIT:
            try:
                status = request.data['status']
                if status == 'CONFIRMED':
                    return Response({'message':'Can only check in 3 hours before appointment.'}, status=status.HTTP_400_BAD_REQUEST)

        super().update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if request.user.is_patient:
            return Response({'message': "Patient cannot delete Appoitnments."}, status=status.HTTP_401_UNAUTHORIZED)
        super().delete(self, request, *args, **kwargs)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def generate_appts(request):
    user = request.user
    if user.is_patient:
        return Response({'message': "Patient cannot create Appoitnments."}, status=status.HTTP_401_UNAUTHORIZED)

    appt_data = JSONParser().parse(request)

    start = request.data['start_time']
    end = request.data['end_time']
    duration = request.data['appt_duration_minutes']
    final_appt = end - timedelta(minutes=duration)
    times = []
    next_appt = start
    while final_appt > next_appt:
        times.append(next_appt)
        next_appt = next_appt + timedelta(minutes=duration)
    
    dates = request.data['dates']
    clinic = request.data['clinic']
    all_appts = []
    for day in dates:
        for time in times:
            instance = Appointment(
                clinic=clinic,
                date_time=time
            )
            instance.save()
            all_appts.append(instance)
    
    # return JsonResponse(all_appts, safe=False)
    return Response(all_appts, safe=False)

