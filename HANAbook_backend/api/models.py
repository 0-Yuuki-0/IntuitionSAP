from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from datetime import datetime

# Create your models here.

MAX_AGE = 65
APPT_STATUS = [
    ('AVAILABLE', 'available'),
    ('BOOKED', 'booked'),
    ('CONFIRMED', 'confirmed')
]


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        '''
        Create and save a user with the given email and password.
        '''
        if not email:
            raise ValueError('email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        '''
        Create and save a superuser with the given email and password.
        '''
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser set to True')
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    is_clinic = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

    addr_line_1 = models.CharField(max_length=255)
    addr_line_2 = models.CharField(max_length=255, null=True, blank=True)
    addr_postcode = models.CharField(max_length=10)
    addr_state = models.CharField(max_length = 200, null=True, blank=True)
    addr_country = models.CharField(max_length=50, default="Singapore")

    USERNAME_FIELD = 'email'  

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Clinic(User):
    name = models.CharField(max_length=255, unique=True)


class Patient(User):
    name = models.CharField(max_length=255, unique=True)
    dob = models.DateField() 
    has_disease_1 = models.BooleanField(default=False)
    has_disease_2 = models.BooleanField(default=False)
    has_disease_3 = models.BooleanField(default=False)
    is_priority = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            # today = datetime.date.today()
            today = datetime.now()
            age = today.year - self.dob.year
            if today.month < self.dob.month or (today.month == self.dob.month and today.day < self.dob.day):
                age -= 1

            if age >= MAX_AGE and (self.has_disease_1 or self.has_disease_2 or self.has_disease_3):
                self.is_priority = True
            elif (self.has_disease_1 and (self.has_disease_2 or self.has_disease_3)) or (self.has_disease_2 and self.has_disease_3):
                self.is_priority = True
            
            super(Patient, self).save(*args, **kwargs)


class Doctor(models.Model):
    name = models.CharField(max_length=255, unique=True)
    specialty = models.CharField(max_length=255)
    clinic = models.ForeignKey(Clinic, to_field='name', db_column='clinic_name', on_delete=models.CASCADE)


class Appointment(models.Model):
    clinic = models.ForeignKey(Clinic, to_field='name', db_column='clinic_name', on_delete=models.CASCADE)
    date_time = models.DateTimeField(null=True, blank=True)
    patient = models.ForeignKey(Patient, to_field='name', db_column='patient_name', on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, to_field='name', db_column='doctor_name', on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=10, choices=APPT_STATUS, default='AVAILABLE')

    def save(self, *args, **kwargs):
        if self.date_time == None:
            self.date_time = datetime.now()