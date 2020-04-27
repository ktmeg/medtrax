from datetime import date
from django.db import models
from django.contrib.auth.models import User

class Meds(models.Model):
    medication = models.CharField(max_length=100, blank=False)
    increments = models.PositiveIntegerField(blank=False, help_text="How many often should this medicine be administered?")
    qty = models.PositiveIntegerField(blank=False, help_text="What quantity to be administered?") 

    def __str__(self):
        return f'{self.medication} {self.qty} to be given every {self.increments}'

    class Meta:
        verbose_name = ('Meds')
        verbose_name_plural = ('Meds')

class Patient(models.Model):
    name = models.CharField(max_length=100, blank=False)
    meds = models.ForeignKey(Meds, on_delete=models.CASCADE, related_name="patients")

    def __str__(self):
        return f'{self.name}'


