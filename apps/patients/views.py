from rest_framework import viewsets, generics, permissions
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from django_filters import rest_framework as filters

from apps.patients.models import PatientCard, DiseaseHistory
from apps.patients.serializers import PatientCardSerializer, DiseaseHistorySerializer, MyPatientsSerializer
from apps.users.models import IsDoctorOrChiefDoctorOrNurse

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PatientCardViewSet(viewsets.ModelViewSet):
    queryset = PatientCard.objects.all()
    serializer_class = PatientCardSerializer
    permission_classes = [IsDoctorOrChiefDoctorOrNurse]
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    filterset_fields = ['gender', 'birth_date', 'nationality']
    search_fields = ['first_name', 'last_name', 'middle_name', 'personal_number', 'phone_number']
    pagination_class = StandardResultsSetPagination


class DiseaseHistoryViewSet(viewsets.ModelViewSet):
    queryset = DiseaseHistory.objects.all()
    serializer_class = DiseaseHistorySerializer
    permission_classes = [IsDoctorOrChiefDoctorOrNurse]
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    filterset_fields = ['disease', 'doctor', 'nurse', 'cured']  # добавлено новое поле
    search_fields = ['disease', 'complaints']
    pagination_class = StandardResultsSetPagination



class MyPatientsView(generics.ListAPIView):
    serializer_class = MyPatientsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'doctor'):
            return DiseaseHistory.objects.filter(doctor=user.doctor, cured=False)
        elif hasattr(user, 'nurse'):
            return DiseaseHistory.objects.filter(nurse=user.nurse, cured=False)
        return DiseaseHistory.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        patient_cards = {history.patient_cart.id: history.patient_cart for history in queryset}
        return Response({
            "patients": list(patient_cards.values()),
            "details": serializer.data
        })
