from django.shortcuts import render
from account_engine.models import Profile
from account_engine.forms import ProfileForm
# Create your views here.


def home(request):

    return render(request, 'index.html')

def edit_profile(request, id):
    profile = Profile.objects.get(id=id)
    form = ProfileForm(instance=profile)
    context = {'profile':profile,"form":form,}

    return render(request, 'edit_profile.html',context)
