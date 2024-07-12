from django.db import models

from apps.users.models import Doctor, Nurse


class PatientCard(models.Model):
    class GenderChoices(models.TextChoices):
        male = 'male', 'male'
        female = 'female', 'female'
        other = 'other', 'other'


    first_name = models.CharField(
        max_length=150,
        verbose_name='имя',
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='фамилия',
    )
    middle_name = models.CharField(
        max_length=150,
        verbose_name='Отчество',
    )   
    photo = models.ImageField(
        upload_to='patient_photo/',
        verbose_name='фото',
    )
    birth_date = models.DateField(
        verbose_name='дата рождения',
    )
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
        verbose_name='пол',
    )
    nationality = models.CharField(
        max_length=150,
        verbose_name='гражданство',
    )
    document_number = models.CharField(
        max_length=150,
        verbose_name='№ документа',
    )
    document_expiry_date = models.DateField(
        verbose_name='срок действия',
    )
    place_of_birth = models.CharField(
        max_length=150,
        verbose_name='Место рождения',
    )
    authority = models.CharField(
        max_length=150,
        verbose_name='Орган выдачи',
    )
    date_of_issue = models.DateField(
        verbose_name='Дата выдачи'
    )
    personal_number = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Персональный номер',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.personal_number}"

    class Meta:
        verbose_name = 'Карта пациента'
        verbose_name_plural = 'Карты пациентов'


class DiseaseHistory(models.Model):
    patient_cart = models.ForeignKey(
        PatientCard,
        on_delete=models.CASCADE,
        related_name='disease_history',
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.SET_NULL,
        null=True,
        related_name='dis_history',
    )
    Nurse = models.ForeignKey(
        Nurse,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='dis_his',
    )
    disease = models.CharField(
        max_length=255,
        verbose_name='название болезни',
    )
    prescription = models.TextField(
        verbose_name='назначение',
    )

    def __str__(self):
        return f"История болезни: {self.disease} для {self.patient_cart.first_name} {self.patient_cart.last_name}"

    class Meta:
        verbose_name = 'История болезни'
        verbose_name_plural = 'Истории болезней'
