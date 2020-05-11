from django.db import models
from django.contrib.auth.models import AbstractUser

# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    username = models.CharField(max_length=20, blank=False, unique=True)
    is_active = models.BooleanField(("active"), default=True)
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=254, unique=True, blank=True)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = []

    def __string__(self):
        return f'{self.first_name} {self.last_name}'
