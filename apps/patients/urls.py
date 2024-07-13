from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.patients.views import PatientCardViewSet, DiseaseHistoryViewSet

router = DefaultRouter()
router.register(r'patient-cards', PatientCardViewSet, basename='patientcard')
router.register(r'disease-history', DiseaseHistoryViewSet, basename='diseasehistory')

urlpatterns = [
    path('', include(router.urls)),
]
