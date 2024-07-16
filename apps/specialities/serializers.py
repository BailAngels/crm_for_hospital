from rest_framework import serializers

from apps.specialities.models import Speciality


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ['id', 'title']