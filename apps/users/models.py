from django.db import models
from django.contrib.auth.models import AbstractUser

from rest_framework import permissions


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'male', 'мужчина'
        FEMALE = 'female', 'женщина'
        OTHER = 'other', 'другое'

    middle_name = models.CharField(
        max_length=150,
        verbose_name='отчество',
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to='user_photo/',
        verbose_name='фото',
        blank=True,
        null=True,
    )
    gender = models.CharField(
        max_length=15,
        choices=GenderChoices.choices,
        verbose_name='пол',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Doctor(User):
    class SpecialityChoices(models.TextChoices):
        INTERNAL_MEDICINE = 'internal_medicine', 'терапевт'
        PEDIATRICS = 'pediatrics', 'педиатр'
        SURGERY = 'surgery', 'хирург'
        CARDIOLOGY = 'cardiology', 'кардиолог'
        NEUROLOGY = 'neurology', 'невролог'
        OPHTHALMOLOGY = 'ophthalmology', 'офтальмолог'

    is_chief_doctor = models.BooleanField(default=False)

    speciality = models.CharField(
        max_length=150,
        choices=SpecialityChoices.choices,
        verbose_name='специальность',
        blank=True,
        null=True,
    )

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
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and (
            isinstance(request.user, Doctor) and request.user.is_chief_doctor
        ) or (
            isinstance(request.user, Doctor) and not request.user.is_chief_doctor
        )

class IsChiefDoctorOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_staff or 
            (isinstance(request.user, Doctor) and request.user.is_chief_doctor)
        )

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_staff