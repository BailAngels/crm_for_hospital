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

   
