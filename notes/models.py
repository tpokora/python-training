from datetime import datetime

from django.conf import settings
from django.db import models
from django.db.models import QuerySet


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

    def __str__(self):
        return 'title: {}, content: {}, user: {}'.format(self.title, self.content, self.user.username)


class NoteQuerySet(QuerySet):

    @staticmethod
    def get_user_past_due_notes(user):
        now = datetime.now()
        past_due_notes = Note.objects.filter(user__id=user.id, due__lt=now)
        return past_due_notes.all()





