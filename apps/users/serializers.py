from rest_framework import serializers
from .models import Doctor, Nurse

class DoctorSerializer(serializers.ModelSerializer):
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


class DoctorCreateSerializerForAdmin(serializers.ModelSerializer):
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
            'is_chief_doctor',
            'speciality'
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        doctor = Doctor(**validated_data)
        doctor.set_password(password)
        doctor.save()
        return doctor


class DoctorCreateByChiefSerializer(serializers.ModelSerializer):
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
            'is_chief_doctor',
            'speciality'
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        doctor = Doctor(**validated_data)
        doctor.set_password(password)
        doctor.save()
        return doctor


class NurseSerializer(serializers.ModelSerializer):
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


class NurseCreateSerializer(serializers.ModelSerializer):
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
    
class DoctorCreateByAdminSerializer(serializers.ModelSerializer):
    """ Создание Доктора Сериализатор для администратора """
    password = serializers.CharField(write_only=True)
    is_chief_doctor = serializers.BooleanField(required=False)  # Поле доступно для записи

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
            'speciality',
            'is_chief_doctor'
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        doctor = Doctor(**validated_data)
        doctor.set_password(password)
        doctor.save()
        return doctor


class NurseCreateSerializerForAdminAndChiefDoctor(serializers.ModelSerializer):
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
