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


class TestUserRegistrationView(TestCase):
    def setUp(self):
        self.url = reverse("user_registration")
        self.username = "testuser"
        self.password = "p12334567"

    def test_user_register_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='user_registration.html')

    def test_register_user(self):
        response = self.client.post(reverse("user_registration"), data={
        "username": self.username,
        "password1": self.password,


        })
        self.assertEqual(response.status_code, 200)

class TestUserLoginView(TestCase):
    def setUp(self):
        self.url = reverse("login")

    def test_user_login_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)



class TestUserLogoutView(TestCase):
    def setUp(self):
        self.url = reverse("user_logout")
        self.user = User.objects.create(username="test",password="password")
        self.cleint = self.client.login(user=self.user,password="pass")

    def test_user_logout_view(self):
        response = self.client.post(reverse)
        self.assertEqual(response.status_code, 302)
