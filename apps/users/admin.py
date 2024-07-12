from django.contrib import admin
from apps.users import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'middle_name', 'is_active']
    search_fields = ['username', 'first_name', 'last_name', 'middle_name']



@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['username']


@admin.register(models.Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ['username']