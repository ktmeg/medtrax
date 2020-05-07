from django import forms
from .models import Meds, Patient
from django_registration.forms import RegistrationForm
from users.models import User


class UserSignUpForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class MedForm(forms.ModelForm):
    class Meta:
        model = Meds
        fields = ['medication', 'increments',
                  'quantity', 'start_date', 'start_time']

# UserCreationForm
