from unittest import TestCase

from django.test import Client


# Create your tests here.
class CoreHomeTests(TestCase):

    def test_home(self):
        client = Client()

        response = client.get('/')
        content = str(response.content)
        text = "<h1>Hello World</h1>"
        self.assertEqual(response.status_code, 200)
        self.assertEqual(text in content, True)

    def test_users(self):
        client = Client()

        response = client.get('/users')
        content = str(response.content)
        header = "<h2>Users</h2>"
        user = "tpokora"
        self.assertEqual(response.status_code, 200)
        self.assertEqual(header in content, True)
        self.assertEqual(user in content, True)
