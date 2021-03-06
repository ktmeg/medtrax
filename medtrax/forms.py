from django import forms
from .models import Meds, Patient
from django_registration.forms import RegistrationForm
from users.models import User


class UserSignUpForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class MedForm(forms.ModelForm):
    class Meta:
        model = Meds
        widgets = {'start_date': DateInput,
                    'start_time': TimeInput}
        fields = ['medication', 'increments', 'unit',
                  'quantity', 'start_date', 'start_time']
