from datetime import datetime

from django.conf import settings
from django.db import models


class Note(models.Model):
    created = models.DateTimeField('created')
    modified = models.DateTimeField('modified', auto_now_add=True, blank=False)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=300)
    due = models.DateTimeField('due', blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def fill(self, data, user):
        self.user = user
        self.title = data['title']
        self.content = data['content']
        self.due = data['due']
        self.created = datetime.now()

