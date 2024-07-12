from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, NurseViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'nurses', NurseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('doctors/register-chief-doctor/', DoctorViewSet.as_view({'post': 'register_chief_doctor'}), name='register-chief-doctor'),
    path('doctors/register-doctor/', DoctorViewSet.as_view({'post': 'register_doctor'}), name='register-doctor'),
    path('nurses/register-nurse/', NurseViewSet.as_view({'post': 'register_nurse'}), name='register-nurse'),
]
