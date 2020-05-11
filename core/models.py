from datetime import date
from django.db import models
from django.contrib.auth.models import User
from users.models import User
from django.utils import timezone


class Meds(models.Model):
    medication = models.CharField(max_length=100, blank=False)
    increments = models.PositiveIntegerField(
        blank=False, help_text="How many often should this medicine be administered?")
    quantity = models.PositiveIntegerField(
        blank=False, help_text="What quantity to be administered?")
    # start_date = models.DateField(auto_now=False, auto_now_add=False)
    # start_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.medication} - {self.quantity} to be given every {self.increments}'

    class Meta:
        verbose_name = ('Meds')
        verbose_name_plural = ('Meds')


class Patient(models.Model):
    name = models.CharField(max_length=100, blank=False)
    meds = models.ForeignKey(
        Meds, on_delete=models.CASCADE, related_name="patients")

    def __str__(self):
        return f'{self.name}'
