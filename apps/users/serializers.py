from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Doctor, Nurse

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'photo', 'gender']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'photo', 'gender', 'is_chief_doctor', 'speciality']

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'photo', 'gender', 'is_busy']

class ChiefDoctorRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Doctor
        fields = ['username', 'first_name', 'last_name', 'middle_name', 'photo', 'gender', 'password']

    def create(self, validated_data):
        validated_data['is_chief_doctor'] = True
        user = Doctor.objects.create_user(**validated_data)
        user.is_superuser = True
        user.save()
        return user

class DoctorRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Doctor
        fields = ['username', 'first_name', 'last_name', 'middle_name', 'photo', 'gender', 'password', 'speciality']

    def create(self, validated_data):
        user = Doctor.objects.create_user(**validated_data)
        user.save()
        return user

class NurseRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Nurse
        fields = ['username', 'first_name', 'last_name', 'middle_name', 'photo', 'gender', 'password']

    def create(self, validated_data):
        user = Nurse.objects.create_user(**validated_data)
        user.save()
        return user
