from congif import settings
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


# class TimeInput(forms.TimeInput):
#     input_type = 'time'


class MedForm(forms.ModelForm):
    start_date = DateInput(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = Meds
        # widget = forms.DateInput(format='%m/%d/%Y')
        fields = ['medication', 'increments',
                  'quantity', 'start_date', 'start_time']


# UserCreationForm
# , 'start_date', 'start_time'
