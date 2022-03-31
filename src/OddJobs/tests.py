from django.test import TestCase
from .models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse

# Create your tests here.

def createTestUser():
    user = User(username="test", type="0", email="test@test.com")
    user.set_password("password")
    user.save()
    return user


class LoginTests(TestCase):
    def test_user_authentication_and_creation(self):
        # Create a new user
        user = createTestUser()

        # Attempt to authenticate newly created user
        userCheck = authenticate(username='test', password='password')

        self.assertIsNotNone(userCheck)

        user.delete()

    def test_logged_in(self):

        user = createTestUser()

        response = self.client.get(reverse('OddJobs:index'))

        # Check that user is not logged in yet
        self.assertNotEquals(first=response.context['request'].user, second=user)

        # Log in user
        login(response.context['request'], user)

        # Check that user is now logged in
        self.assertEquals(first=response.context['request'].user, second=user)

        # Delete test user

        user.delete()


