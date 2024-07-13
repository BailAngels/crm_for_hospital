from rest_framework import viewsets, response, decorators, status
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter  # Импортируйте SearchFilter отсюда
from .models import Doctor, Nurse
from .serializers import (
    DoctorSerializer,
    NurseSerializer,
    DoctorCreateSerializer,
    NurseCreateSerializer
)
from apps.users.models import IsChiefDoctorOrAdmin, IsAdminOrReadOnly

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsChiefDoctorOrAdmin]
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    filterset_fields = ['speciality', 'is_chief_doctor']
    search_fields = ['username', 'first_name', 'last_name', 'speciality']
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'register_chief_doctor':
            return DoctorCreateSerializer
        return self.serializer_class

    @decorators.action(detail=False, methods=['post'], permission_classes=[IsAdminOrReadOnly])
    def register_chief_doctor(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(is_chief_doctor=True)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
    permission_classes = [IsChiefDoctorOrAdmin]
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    filterset_fields = ['is_busy']
    search_fields = ['username', 'first_name', 'last_name']
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action == 'create':
            return NurseCreateSerializer
        return self.serializer_class
