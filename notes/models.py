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

    @staticmethod
    def fill(data, user):
        note = Note()
        note.user = user
        note.title = data['title']
        note.content = data['content']
        note.due = data['due']
        note.created = datetime.now()
        return note

