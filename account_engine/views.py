from django.shortcuts import render, redirect
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


def user_profile(request):
    
    return render (request, 'user_profile.html')

def edit_profile(request, id):
    profile = Profile.objects.get(id=id)
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {'profile':profile,"form":form,}

    return render(request, 'edit_profile.html',context)
