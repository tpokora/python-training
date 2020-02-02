from unittest import TestCase

from django.test import Client
from django.urls import reverse

# Create your tests here.
from core.models import User, UserConfiguration


class CoreTests(TestCase):

    @staticmethod
    def create_test_user():
        user = User.objects.filter(username='testUser')
        if user.count() == 0:
            user = User()
            user.username = 'testUser'
            user.password = 'testPassword'
            user.email = 'testUser@email.com'
            user.save()
            user = User.objects.filter(username='testUser')
        return user.get()

    def test_user__str__(self):
        user = CoreTests.create_test_user()
        expected_user_str = 'id: {}, username: {}, email: {}'.format(user.pk, user.username, user.email)

        self.assertEqual(user.__str__(), expected_user_str, True)

    def test_configuration__str__(self):
        user = CoreTests.create_test_user()
        configuration = UserConfiguration()
        configuration.user = user

        expected_conf_str = "user: '{}'".format(configuration.user.__str__())

        self.assertEqual(configuration.__str__(), expected_conf_str, True)


class CoreViewTests(TestCase):
    H1_TAG = '<h1>'
    H1_TAG_CLOSE = '</h1>'
    H2_TAG = '<h2>'
    H2_TAG_CLOSE = '</h2>'
    H3_TAG = '<h3>'
    H3_TAG_CLOSE = '</h3>'
    P_TAG = '<p>'
    P_TAG_CLOSE = '</p>'

    def test_home_user_not_authorized(self):
        client = Client()

        login = "Login</a>"
        response = client.get(reverse("core:index"))
        content = str(response.content)
        welcome = "{}Welcome!{}".format(self.H1_TAG, self.H1_TAG_CLOSE)
        text = "{}Please login to view content{}".format(self.H2_TAG, self.H2_TAG_CLOSE)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(welcome in content, True)
        self.assertEqual(text in content, True)
        self.assertEqual(login in content, True)

    def test_home_user_is_authorized(self):
        client = Client()

        user = CoreTests.create_test_user()
        client.force_login(user=user)
        response = client.get(reverse("core:index"))
        content = str(response.content)
        welcome = "{}Welcome, {}!{}".format(self.H1_TAG, user.username, self.H1_TAG_CLOSE)
        text = 'href="/user/%s"' % user.id
        self.assertEqual(response.status_code, 200)
        self.assertEqual(welcome in content, True)
        self.assertEqual(text in content, True)
        logged_as = "Logged as: %s" % user.username
        self.assertEqual(logged_as in content, True)
        logout = "Logout"
        self.assertEqual(logout in content, True)

    def test_users(self):
        client = Client()

        users = User.objects.all()
        response = client.get(reverse("core:users"))
        content = str(response.content)
        header = "{}Users{}".format(self.H2_TAG, self.H2_TAG_CLOSE)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(header in content, True)
        for user in users:
            self.assertEqual(user.username in content, True)

    def test_user_pk1(self):
        client = Client()

        user = CoreTests.create_test_user()
        client.force_login(user=user)
        response = client.get(reverse("core:user", args=(user.id,)))
        content = str(response.content)
        user_header = "%s%s%s" % (self.H2_TAG, user.username, self.H2_TAG_CLOSE)
        user_email = "%sEmail: %s%s" % (self.P_TAG, user.email, self.P_TAG_CLOSE)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(user_header in content, True, "%s is not having %s" % (user_header, user.username))
        self.assertEqual(user_email in content, True, "%s is not having %s" % (user_email, user.email))

    def test_user_pk_not_authorized(self):
        client = Client()

        response = client.get(reverse("core:user", args=(1,)))
        self.assertEqual(response.status_code, 302)
