from datetime import date, time
from django.utils.timezone import now
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
    MedUnits = models.TextChoices('MedUnits', 'Hours Days Month')
    unit = models.CharField(
        blank=False, choices=MedUnits.choices, max_length=30, default='misc')
    start_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    start_time = models.TimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return f'{self.medication} - {self.quantity} to be given every {self.increments} {self.unit}'

    class Meta:
        verbose_name = ('Meds')
        verbose_name_plural = ('Meds')


class Patient(models.Model):
    name = models.CharField(max_length=100, blank=False)
    meds = models.ForeignKey(
        Meds, on_delete=models.CASCADE, related_name="patients")

    def __str__(self):
        return f'{self.name}'


# auto_now_add=False, auto_now=False, default=None
