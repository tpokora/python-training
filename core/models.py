from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return "id: {}, username: {}, email: {}".format(self.pk, self.username, self.email)


class UserConfiguration(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "user: '{}'".format(self.user.__str__())
