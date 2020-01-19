import datetime
from unittest import TestCase

# Create your tests here.
from django.test import Client

from core.tests import CoreTests
from notes.forms import NoteForm
from notes.models import Note, NoteQuerySet

DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


class NotesTests(TestCase):

    def test_create_note_for_user(self):
        user = CoreTests.create_test_user()
        test_note = NoteTestsHelper.create_note(user)
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
        note = Note()
        note.fill(note_data, user)

        self.assertEqual(note.title == note_data['title'], True)
        self.assertEqual(note.content == note_data['content'], True)
        self.assertEqual(note.created.strftime(DATE_TIME_FORMAT) == datetime.datetime.now().strftime(DATE_TIME_FORMAT),
                         True)
        self.assertEqual(note.due.strftime(DATE_TIME_FORMAT) == note_data['due'].strftime(DATE_TIME_FORMAT),
                         True)
        self.assertEqual(note.user == user, True)

    def test_note_form_valid(self):
        form_data = {'title': 'test title', 'content': 'test content', 'due': datetime.datetime.now()}
        form = NoteForm(data=form_data)
        self.assertTrue(form.is_valid())


class NoteQuerySetTests(TestCase):

    NOW = datetime.datetime.now()

    def test_get_notes_quantity(self):
        user = CoreTests.create_test_user()
        test_note_before_due = NoteTestsHelper.create_note(user)
        test_note_past_due = NoteTestsHelper.create_note(user)
        test_note_past_due.due = self.NOW - datetime.timedelta(days=3)

        self.assertEqual(test_note_before_due.due > self.NOW, True)
        self.assertEqual(test_note_past_due.due < self.NOW, True)

        test_note_before_due.save()
        test_note_past_due.save()
        past_due_notes = NoteQuerySet.get_user_past_due_notes(user)

        self.assertEqual(len(past_due_notes) == 1, True)

        test_note_before_due.delete()
        test_note_past_due.delete()


class NoteTestsHelper():

    @staticmethod
    def create_note(user):
        note = Note()
        note.user = user
        note.title = 'Test note Title'
        note.content = 'Test note content Test note content Test note content Test note content'
        note.due = datetime.datetime.now() + datetime.timedelta(days=3)
        note.created = datetime.datetime.now()
        return note








