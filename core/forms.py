from django import forms
from .models import Meds, Patient 


class MedForm(forms.ModelForm):
    class Meta:
        model = Meds
        fields = ['medication', 'increments', 'quantity', 'start_date', 'start_time']