from rest_framework import serializers, validators
from .models import Doctor, Nurse

class DoctorSerializer(serializers.ModelSerializer):
    """ Доктор Сериализатор """
    class Meta:
        model = Doctor
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'middle_name',
            'photo',
            'gender',
            'is_chief_doctor',
            'speciality'
        ]

class NurseSerializer(serializers.ModelSerializer):
    """ Медсестра Сериализатор """
    class Meta:
        model = Nurse
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'middle_name',
            'photo',
            'gender',
            'is_busy'
        ]

class DoctorCreateSerializer(serializers.ModelSerializer):
    """ Создание Доктора Сериализатор """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Doctor
        fields = [
            'username',
            'first_name',
            'last_name',
            'middle_name',
            'photo',
            'gender',
            'password',
            'speciality'
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        doctor = Doctor(**validated_data)
        doctor.set_password(password)
        doctor.save()
        return doctor

class NurseCreateSerializer(serializers.ModelSerializer):
    """ Создание Медсестры Сериализатор """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Nurse
        fields = [
            'username',
            'first_name',
            'last_name',
            'middle_name',
            'photo',
            'gender',
            'password'
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        nurse = Nurse(**validated_data)
        nurse.set_password(password)
        nurse.save()
        return nurse
