from django import forms
from .models import Meds, Patient
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class MedForm(forms.ModelForm):
    class Meta:
        model = Meds
        fields = ['medication', 'increments',
                  'quantity', 'start_date', 'start_time']
