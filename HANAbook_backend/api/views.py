from django.shortcuts import render

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

# api for clinic to generate weekday sched, and weekend sched

# Create your views here.

list clinic, patient, appt

create clinic, patient, appt

update appt

delete appt

-
auto appt
    date list,start time, end time, duration, clinic

