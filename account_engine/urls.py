from django.urls import path
from account_engine.views import (home, edit_profile)

urlpatterns = [
path('',home,name="home"),
path('edit-profile/<int:id>/', edit_profile,name="edit_profile")
]
