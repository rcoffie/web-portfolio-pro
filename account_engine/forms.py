from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.gis import forms
from django.core.exceptions import ValidationError
from django.forms import FloatField, Form

from .models import Profile
import floppyforms.__future__ as forms

class OsmPointWidget(forms.gis.PointWidget, forms.gis.BaseOsmWidget):
    pass


class ProfileForm(forms.ModelForm):
    location = forms.gis.PointField(
        widget=OsmPointWidget(
            attrs={
                "map_width": 1000,
                "map_height": 700,
            }
        )
    )

    class Meta:
        model = Profile
        fields = ("phone_number", "home_address", "first_name", "last_name", "location")


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
