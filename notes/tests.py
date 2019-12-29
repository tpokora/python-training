from datetime import datetime
from unittest import TestCase

# Create your tests here.
from django.test import Client

from core.tests import CoreTests
from notes.models import Note


class NotesTests(TestCase):

    @staticmethod
    def create_note(user):
        note = Note()
        note.user = user
        note.title = 'Test note Title'
        note.content = 'Test note content Test note content Test note content Test note content'
        note.created = datetime.now()
        return note

    def test_create_note_for_user(self):
        user = CoreTests.create_test_user()
        test_note = self.create_note(user)
        test_note.save()

        saved_note = Note.objects.get(pk=test_note.id)
        self.assertEqual(test_note == saved_note, True)

        saved_note.delete()

        self.assertRaises(Note.DoesNotExist, Note.objects.get, pk=saved_note.id)



