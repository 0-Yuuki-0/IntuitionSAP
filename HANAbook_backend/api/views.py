from django.shortcuts import render
from api.models import *
from api.serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from datetime import datetime, timedelta
from rest_framework import permissions

# from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes

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
        name = self.request.query_params.get('name')
        if name != None:
            qs = qs.filter(name=name)
        
        return qs

    def perform_create(self, serializer):
        serializer.save(is_clinic=True)
        

class PatientListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs = Patient.objects.all()
        user = self.request.user

        # custom filters
        name = self.request.query_params.get('name')
        if name != None:
            qs = qs.filter(name=name)

        # filter by permissions
        if user.is_anonymous:
            return Patient.objects.none()
        elif user.is_patient:
            qs = qs.filter(id=user.id)
        
        return qs

    def perform_create(self, serializer):
        serializer.save(is_patient=True)


class PatientRetriveDestroyAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Patient.objects.all()

        # filter by permissions
        user = self.request.user
        if user.is_patient:
            qs = qs.filter(id=user.id)
        
        return qs
    
    def delete(self, request, *args, **kwargs):
        return Response({'message':'Unimplemented.'}, status=status.HTTP_401_UNAUTHORIZED)


class AppointmentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Appointment.objects.all()

        # custom filters
        clinic = self.request.query_params.get('clinic')
        patient = self.request.query_params.get('patient')
        status = self.request.query_params.get('status')
        date_time = self.request.query_params.get('date_time')
        if clinic != None:
            qs = qs.filter(clinic=clinic)
        if patient != None:
            qs = qs.filter(patient=patient)
        if status != None:
            qs = qs.filter(status=status)
        if date_time != None:
            qs = qs.filter(date_time=date_time)
        
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
            except:
                pass
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


class DoctorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        if user.is_patient:
            return Response({'message': "Patient cannot create Doctors."}, status=status.HTTP_401_UNAUTHORIZED)
        if user.is_clinic:
            clinic = Clinic.objects.get(id=user.id)
            request.data['clinic'] = clinic.name
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def get_appt(request):
    user = request.user
    if not user.is_patient:
        return Response({'message': "Only Patient has access to this."}, status=status.HTTP_401_UNAUTHORIZED)

    sched_data = JSONParser().parse(request)
    time = request.data['date']

    # get clinics in postcode
    # get available appts on date

    cust_postcode = user.addr_postcode
    clinics = Clinic.objects.filter(id__addr_postcode=cust_postcode)
    all_appts = Appointment.objects.none()
    for clinic in clinics:
        appts = Appointment.objects.filter(status='AVAILABLE').filter(clinic=clinic.name)
        all_appts |= appts
    
    return Response(all_appts, safe=False)


