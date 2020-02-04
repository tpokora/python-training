from django.contrib.postgres.fields import JSONField
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return "id: {}, username: {}, email: {}".format(self.pk, self.username, self.email)

    def create_user_configuration(self):
        configuration = UserConfiguration.objects.filter(user__id=self.pk)
        if configuration.count() == 0:
            configuration = UserConfiguration()
            configuration.user = self
            configuration.save()

    def get_user_configuration(self):
        configuration = UserConfiguration.objects.filter(user__id=self.pk)
        return configuration.get()


class Configuration:
    DEFAULT_CONFIGURATION = dict({'visible': True})


class UserConfiguration(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    configuration = JSONField(null=False, blank=False, default=Configuration.DEFAULT_CONFIGURATION)

    def __str__(self):
        return "user: '{}', configuration: {}".format(self.user.__str__(), self.configuration)

