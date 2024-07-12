from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, NurseViewSet, ChiefDoctorRegistrationView, DoctorRegistrationView, NurseRegistrationView

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'nurses', NurseViewSet)

urlpatterns = [
    path('register/chief_doctor/', ChiefDoctorRegistrationView.as_view(), name='register-chief-doctor'),
    path('register/doctor/', DoctorRegistrationView.as_view(), name='register-doctor'),
    path('register/nurse/', NurseRegistrationView.as_view(), name='register-nurse'),
]

urlpatterns += router.urls
