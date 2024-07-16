from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import permissions

from apps.speciality.models import Speciality


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'male', 'мужчина'
        FEMALE = 'female', 'женщина'
        OTHER = 'other', 'другое'

    middle_name = models.CharField(
        max_length=150,
        verbose_name='отчество',
    )
    photo = models.ImageField(
        upload_to='user_photo/',
        verbose_name='фото',
    )
    gender = models.CharField(
        max_length=15,
        choices=GenderChoices.choices,
        verbose_name='пол'
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Doctor(User):
    is_chief_doctor = models.BooleanField(default=False)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, verbose_name='специальность')

    def __str__(self):
        return f"Doctor: {self.username}"

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'


class Nurse(User):
    is_busy = models.BooleanField(default=False)

    def __str__(self):
        return f'Nurse: {self.username}'

    class Meta:
        verbose_name = 'Медсестра'
        verbose_name_plural = 'Медсестры'


class IsDoctorOrChiefDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.is_staff:
                return True
            if hasattr(request.user, 'doctor'):
                return request.user.doctor.is_chief_doctor or request.user.doctor
        return False


class IsChiefDoctorOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.is_staff:
                return True
            if isinstance(request.user, Doctor) and request.user.is_chief_doctor:
                return True
        return False


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsChiefDoctorOrAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user and request.user.is_authenticated:
            if request.user.is_staff:
                return True
            if isinstance(request.user, Doctor) and request.user.is_chief_doctor:
                return True
        return False
    

class IsAdmin(permissions.BasePermission):
    """
    Разрешение только для администратора.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsAdminOrChiefDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.is_staff:
                return True
            if isinstance(request.user, Doctor) and request.user.is_chief_doctor:
                return True
        return False
