from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.patients.views import PatientCardViewSet, DiseaseHistoryViewSet, MyPatientsView, DoctorsPatientsView

router = DefaultRouter()
router.register(r'patient-cards', PatientCardViewSet, basename='patientcard')
router.register(r'disease-history', DiseaseHistoryViewSet, basename='diseasehistory')

urlpatterns = [
    path('', include(router.urls)),
    path('my-patients/', MyPatientsView.as_view(), name='my-patients'),
    path('doctors-patients/', DoctorsPatientsView.as_view(), name='doctors-patients'),
]

