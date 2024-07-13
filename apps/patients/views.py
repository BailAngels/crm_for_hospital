from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter  # Исправьте импорт
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from apps.patients.models import PatientCard, DiseaseHistory
from apps.patients.serializers import PatientCardSerializer, DiseaseHistorySerializer
from apps.users.models import IsDoctorOrChiefDoctor

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PatientCardViewSet(viewsets.ModelViewSet):
    queryset = PatientCard.objects.all()
    serializer_class = PatientCardSerializer
    permission_classes = [IsDoctorOrChiefDoctor]
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]  # Исправьте импорт
    filterset_fields = ['gender', 'birth_date', 'nationality']  # Example fields for filtering
    search_fields = ['first_name', 'last_name', 'middle_name', 'personal_number']
    pagination_class = StandardResultsSetPagination

class DiseaseHistoryViewSet(viewsets.ModelViewSet):
    queryset = DiseaseHistory.objects.all()
    serializer_class = DiseaseHistorySerializer
    permission_classes = [IsDoctorOrChiefDoctor]
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]  # Исправьте импорт
    filterset_fields = ['disease', 'doctor', 'Nurse']  # Example fields for filtering
    search_fields = ['disease']
    pagination_class = StandardResultsSetPagination

    def create(self, request, *args, **kwargs):
        patient_data = request.data.get('patient', {})
        history_data = request.data.get('history', {})

        # Check if the patient card exists
        personal_number = patient_data.get('personal_number')
        try:
            patient_card = PatientCard.objects.get(personal_number=personal_number)
        except PatientCard.DoesNotExist:
            # Create a new patient card
            patient_serializer = PatientCardSerializer(data=patient_data)
            if patient_serializer.is_valid():
                patient_card = patient_serializer.save()
            else:
                return Response(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Create a new disease history for the patient
        history_data['patient_cart'] = patient_card.id
        history_serializer = DiseaseHistorySerializer(data=history_data)
        if history_serializer.is_valid():
            history_serializer.save(doctor=request.user)
            return Response(history_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(history_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
