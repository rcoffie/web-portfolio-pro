from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       PasswordResetForm, UserCreationForm)
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic import TemplateView

from account_engine.forms import LoginForm, ProfileForm, RegistrationForm
from account_engine.models import Profile

# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"

    def profiles(self):
        profiles = Profile.objects.all()
        return serializers.serialize("geojson", profiles)


@login_required(login_url="/login/")
def user_profile(request, id):

    profile = Profile.objects.get(id=id)
    if request.user == profile.user:
        context = {"profile": profile}
        return render(request, "user_profile.html", context)
    else:
        return redirect("home")


@login_required(login_url="/login/")
def edit_profile(request, id):
    profile = Profile.objects.get(id=id)
    if request.user == profile.user:
        form = ProfileForm(instance=profile)
        if request.method == "POST":
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                return redirect("home")
        context = {"profile": profile, "form": form}
        return render(request, "edit_profile.html", context)
    else:
        return redirect("home")


def user_registration(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                profile.objects.create(user=new_user)
                return redirect("home")
        else:
            form = RegistrationForm()
        return render(request, "user_registration.html", {"form": form})


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "user_login.html"


@login_required(login_url="/login/")
def user_logout(request):
    logout(request)
    return redirect("home")
