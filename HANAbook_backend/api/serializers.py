from rest_framework import serializers
from api.models import *
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = '__all__'
        read_only_fields = (
            'is_staff', 'is_active', 'date_joined', 'is_clinic', 'is_patient'
        )


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data['password']
        password = make_password(password)
        validated_data.update({'password':password})
        try:
            instance = Clinic._default_manager.create(**validated_data)
        except TypeError:
            raise TypeError('TypeError')
        return instance


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_field = ('is_priority')
        
    def create(self, validated_data):
        password = validated_data['password']
        password = make_password(password)
        validated_data.update({'password':password})
        try:
            instance = Patient._default_manager.create(**validated_data)
        except TypeError:
            raise TypeError('TypeError')
        return instance


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

