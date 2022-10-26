from django.test import TestCase
from account_engine.models import Profile
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client

class TestEditUserView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="pass")
        self.profile = Profile.objects.create(user=self.user)

        self.client = Client()



    def test_edit_user_profile_view(self):
        print(self.user.profile)
        self.cleint = self.client.login(user=self.user,password="pass")
        response = self.client.get(reverse('edit_profile', args=[1]), {'user_id': self.user.id})

        data = {
        "phone_number":"888484",
        "home_address": "updated home",
        "status":True
        }
        url = self.client.post(reverse('edit_profile',args=[1]), data=data)
        self.assertEqual(url.status_code, 302)


class TestUserProfileDetailView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="profile_details", password="pass")

    def test_user_profile_view(self):
        user_profile = Profile.objects.create(user=self.user, phone_number="234545", home_address="test")
        response = self.client.get(reverse('user_profile', args=[1]))
        self.assertEqual(response.status_code, 302)
