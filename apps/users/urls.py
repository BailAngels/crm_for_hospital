from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, NurseViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'nurses', NurseViewSet, basename='nurse')

urlpatterns = [
    path('', include(router.urls)),
    path('doctors/register-chief-doctor/', DoctorViewSet.as_view({'post': 'register_chief_doctor'}), name='register-chief-doctor'),
]
