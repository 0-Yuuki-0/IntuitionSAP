from api.views import *
from django.urls import path, include

clinic_patterns = [
    path('', ClinicListCreateAPIView.as_view())
]

patient_patterns = [
    path('', PatientListCreateAPIView.as_view()),
    path('<str:pk>/', PatientRetriveDestroyAPIView.as_view())
]

appointment_patterns = [
    path('', AppointmentListCreateAPIView.as_view()),
    path('<str:pk>/', AppointmentRetrieveDestroyAPIView.as_view())
]

auto_patterns = [
    path('generate/', generate_appts),
    path('get_appt/', get_appt)
]

doctor_patterns = [
    path('', DoctorListCreateAPIView.as_view())
]

urlpatterns = [
    path('clinics/', include(clinic_patterns)),
    path('patients/', include(patient_patterns)),
    path('appointments/', include(appointment_patterns)),
    path('doctors/', include(doctor_patterns)),
    path('token/get_user/', UserListAPIView.as_view()),
    path('auto/', include(auto_patterns))
]