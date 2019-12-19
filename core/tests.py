from unittest import TestCase

from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse


# Create your tests here.
class CoreHomeTests(TestCase):

    def test_home(self):
        client = Client()

        response = client.get(reverse("core:index"))
        content = str(response.content)
        text = "<h1>Hello World</h1>"
        self.assertEqual(response.status_code, 200)
        self.assertEqual(text in content, True)

    def test_users(self):
        client = Client()

        users = User.objects.all()

        response = client.get(reverse("core:users"))
        content = str(response.content)
        header = "<h2>Users</h2>"
        self.assertEqual(response.status_code, 200)
        self.assertEqual(header in content, True)
        for user in users:
            self.assertEqual(user.username in content, True)

    def test_user_pk1(self):
        client = Client()

        user = User.objects.get(pk=1)

        response = client.get(reverse("core:user", args=(user.id,)))
        content = str(response.content)
        header = "<h2>User"
        self.assertEqual(response.status_code, 200)
        self.assertEqual(header in content, True)
        self.assertEqual(user.username in content, True)
