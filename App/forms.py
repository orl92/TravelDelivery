from attr import field
from click import password_option
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from more_itertools import first


class CustomUserCreationForm(UserCreationForm):
    pass

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
