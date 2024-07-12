from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Doctor, Nurse

User = get_user_model()

class DoctorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'photo', 'gender', 'password', 'is_chief_doctor', 'speciality']
        extra_kwargs = {'is_chief_doctor': {'read_only': True}}

    def create(self, validated_data):
        user = Doctor.objects.create_user(**validated_data)
        user.save()
        return user

class NurseSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Nurse
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'photo', 'gender', 'password', 'is_busy']

    def create(self, validated_data):
        user = Nurse.objects.create_user(**validated_data)
        user.save()
        return user
