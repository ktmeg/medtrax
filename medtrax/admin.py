from django.contrib import admin
from .models import Patient, Meds, Log

admin.site.register(Patient)
admin.site.register(Meds)
admin.site.register(Log)