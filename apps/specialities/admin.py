from django.contrib import admin
from .models import Speciality

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)