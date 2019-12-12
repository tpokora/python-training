from django.test import TestCase, Client


# Create your tests here.
from django.test.utils import setup_test_environment


class CoreHomeTests(TestCase):

    def test_home(self):
        client = Client()

        response = client.get('/home/')
        content = str(response.content)
        text = "<h1>Hello World</h1>"
        self.assertEqual(response.status_code, 200)
        self.assertEqual(text in content, True)

