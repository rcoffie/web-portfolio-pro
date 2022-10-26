from django.test import TestCase
from account_engine.models import Profile
from django.contrib.auth.models import User

class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")


    def test_model_str(self):
        user_profile = Profile.objects.create(user=self.user)
        self.assertEqual(str(user_profile), "test")
