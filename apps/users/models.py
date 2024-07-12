from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import permissions

class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        male = 'male', 'мужчина'
        female = 'female', 'женщина'
        other = 'other', 'другое'

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
    class SpecialityChoices(models.TextChoices):
        internal_medicine = 'internal_medicine', 'терапевт'
        pediatrics = 'pediatrics', 'педиатр'
        surgery = 'surgery', 'хирург'
        cardiology = 'cardiology', 'кардиолог'
        neurology = 'neurology', 'невролог'
        ophthalmology = 'ophthalmology', 'офтальмолог'

    is_chief_doctor = models.BooleanField(default=False)

    speciality = models.CharField(
        max_length=150,
        choices=SpecialityChoices.choices,
        verbose_name='специальность',
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


class IsChiefDoctorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_chief_doctor

class IsDoctorOrChiefDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and (
            isinstance(request.user, Doctor) and request.user.is_chief_doctor
        ) or (
            isinstance(request.user, Doctor) and not request.user.is_chief_doctor
        )

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_staff