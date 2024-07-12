from django.contrib import admin

from apps.patients.models import PatientCard, DiseaseHistory


@admin.register(PatientCard)
class PatientCardAdmin(admin.ModelAdmin):
    list_display = ['first_name']


@admin.register(DiseaseHistory)
class DiseaseHistoryAdmin(admin.ModelAdmin):
    list_display = ['disease']
