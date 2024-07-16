from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from .models import Doctor, Nurse
from .serializers import (
    DoctorSerializer,
    NurseSerializer,
    NurseCreateSerializerForAdminAndChiefDoctor,
    DoctorCreateByAdminSerializer,
    DoctorCreateByChiefSerializer,
    NurseCreateSerializer,
)
from apps.users.models import IsChiefDoctorOrAdminOrReadOnly

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    filterset_fields = ['speciality', 'is_chief_doctor']
    search_fields = ['username', 'first_name', 'last_name', 'speciality__name']
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        user = self.request.user
        if user.is_staff and not isinstance(user, Doctor):  # Если пользователь администратор
            return DoctorCreateByAdminSerializer
        if isinstance(user, Doctor) and user.is_chief_doctor:  # Если пользователь главврач
            return DoctorCreateByChiefSerializer
        return DoctorSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if isinstance(user, Doctor) and user.is_chief_doctor:
            # Если главврач создает доктора, устанавливаем is_chief_doctor на False
            serializer.save(is_chief_doctor=False)
        else:
            serializer.save()


class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    filterset_fields = ['is_busy']
    search_fields = ['username', 'first_name', 'last_name']
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            user = self.request.user
            if user.is_staff or (isinstance(user, Doctor) and user.is_chief_doctor):
                return NurseCreateSerializerForAdminAndChiefDoctor
            return NurseCreateSerializer
        return NurseSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [permission() for permission in self.permission_classes]
        return [permission() for permission in self.permission_classes]