import datetime
from unittest import TestCase

# Create your tests here.
from django.test import Client

from core.tests import CoreTests
from notes.models import Note

DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


class NotesTests(TestCase):

    @staticmethod
    def create_note(user):
        note = Note()
        note.user = user
        note.title = 'Test note Title'
        note.content = 'Test note content Test note content Test note content Test note content'
        note.due = datetime.datetime.now() + datetime.timedelta(days=3)
        note.created = datetime.datetime.now()
        return note

    def test_create_note_for_user(self):
        user = CoreTests.create_test_user()
        test_note = self.create_note(user)
        test_note.save()

        saved_note = Note.objects.get(pk=test_note.id)
        self.assertEqual(test_note.id == saved_note.id, True)
        self.assertEqual(test_note.title == saved_note.title, True)
        self.assertEqual(test_note.content == saved_note.content, True)
        self.assertEqual(test_note.created.strftime(DATE_TIME_FORMAT) == saved_note.created.strftime(DATE_TIME_FORMAT), True)
        self.assertEqual(test_note.modified.strftime(DATE_TIME_FORMAT) == saved_note.modified.strftime(DATE_TIME_FORMAT), True)
        self.assertEqual(test_note.user == saved_note.user, True)

        saved_note.delete()

        self.assertRaises(Note.DoesNotExist, Note.objects.get, pk=saved_note.id)

    def test_note_fill(self):
        user = CoreTests.create_test_user()
        note_data = {'title': 'test title', 'content': 'test content', 'due': datetime.datetime.now()}
        note = Note.fill(note_data, user)

        self.assertEqual(note.title == note_data['title'], True)
        self.assertEqual(note.content == note_data['content'], True)
        self.assertEqual(note.created.strftime(DATE_TIME_FORMAT) == datetime.datetime.now().strftime(DATE_TIME_FORMAT),
                         True)
        self.assertEqual(note.due.strftime(DATE_TIME_FORMAT) == note_data['due'].strftime(DATE_TIME_FORMAT),
                         True)
        self.assertEqual(note.user == user, True)




