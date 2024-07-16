from django.db import models


class Speciality(models.Model):
    title = models.CharField(max_length=150, verbose_name='название специальности')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'
