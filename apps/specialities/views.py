from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter

from apps.specialities.models import Speciality
from apps.specialities.serializers import SpecialitySerializer

from apps.users.models import IsAdminOrReadOnly
from apps.users.views import StandardResultsSetPagination


class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title']