from rest_framework import serializers
from .models import PatientCard, DiseaseHistory

class PatientCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientCard
        fields = [
            'id', 'first_name', 'last_name', 'middle_name', 'photo',
            'birth_date', 'gender', 'nationality', 'document_number',
            'document_expiry_date', 'place_of_birth', 'authority',
            'date_of_issue', 'personal_number', 'phone_number'
        ]

class DiseaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseHistory
        fields = [
            'id', 'patient_cart', 'doctor', 'nurse', 'disease',
            'prescription', 'complaints', 'cured'
        ]


class MyPatientsSerializer(serializers.ModelSerializer):
    patient = serializers.CharField(source='patient_cart.__str__')

    class Meta:
        model = DiseaseHistory
        fields = ['id', 'patient_cart', 'disease', 'prescription', 'complaints', 'cured']
        read_only_fields = ['id', 'patient_cart', 'disease', 'prescription', 'complaints', 'cured']
