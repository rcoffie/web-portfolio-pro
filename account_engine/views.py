from django.shortcuts import render
from account_engine.models import Profile
from account_engine.forms import ProfileForm
from django.views.generic import TemplateView
from django.core import serializers
from django.http import HttpResponse
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'
    def profiles(self):
        profiles = Profile.objects.all()
        return serializers.serialize('geojson', profiles)

def edit_profile(request, id):
    profile = Profile.objects.get(id=id)
    form = ProfileForm(instance=profile)
    context = {'profile':profile,"form":form,}

    return render(request, 'edit_profile.html',context)
