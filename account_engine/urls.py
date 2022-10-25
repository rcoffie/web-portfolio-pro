from django.urls import path
from account_engine.views import (HomeView, edit_profile, user_profile, user_registration, LoginView, user_logout)

urlpatterns = [
# path('',home,name="home"),
path('',HomeView.as_view(), name="home"),
path('edit-profile/<int:id>/', edit_profile,name="edit_profile"),
path('user-profile/<int:id>/', user_profile, name="user_profile"),
path('user-registration/', user_registration, name="user_registration"),
path('login/', LoginView.as_view(), name='login'),
path('user-logout/',user_logout, name="user_logout"),
]
