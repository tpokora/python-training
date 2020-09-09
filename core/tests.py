from django.contrib.auth.models import User
from django.test import TestCase, Client


# Create your tests here.
class BasicTestCase(TestCase):

    TEST_USER = 'testUser'
    TEST_USER_PASSWORD = '12345'

    def create_test_user(self, username, password):
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return user


class CoreHomeTests(BasicTestCase):

    def test_home(self):
        client = Client()

        response = client.get('/')
        content = str(response.content)
        text = "<h1>Hello World</h1>"
        self.assertEqual(response.status_code, 200)
        self.assertEqual(text in content, True)
