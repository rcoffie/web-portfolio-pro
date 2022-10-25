from django import forms
from .models import Profile
from django.forms import Form, FloatField
from django.contrib.gis import forms

import floppyforms.__future__ as forms

class OsmPointWidget(forms.gis.PointWidget, forms.gis.BaseOsmWidget):
    pass

class ProfileForm(forms.ModelForm):
    location = forms.gis.PointField(widget=OsmPointWidget(attrs={
        'map_width': 1000,
        'map_height': 700,
    }))

    class Meta:
        model = Profile
        fields = ('phone_number','home_address','first_name','last_name','location')
