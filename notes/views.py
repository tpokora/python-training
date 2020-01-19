from datetime import datetime

from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, TemplateView

from notes.forms import NoteForm
from notes.models import Note
from notes.utils import NoteUtils


class UserNotesView(ListView):
    template_name = 'notes/user_notes.html'
    context_object_name = 'user_notes'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')
        return super().get(self, request, *args, **kwargs)

    def get_queryset(self):
        user_id = self.request.user.pk
        user_notes = Note.objects.filter(user__id=user_id)
        return user_notes

        # note = Note()
        # note.title = 'Note Title'
        # note.content = 'Note content test Note content test Note content test Note content test'
        # note.created = datetime.now()
        #
        # notes = []
        # notes.append(note)
        # notes.append(note)
        # return notes

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        NoteUtils.context_add_user_past_due_notes(context, self.request)
        context['submitted'] = 'submitted' in self.request.GET
        context['form'] = NoteForm()
        return context


def note_delete(request, note_id):
    if not request.user.is_authenticated:
        return redirect('/')
    note = Note.objects.filter(pk=note_id)
    note.delete()
    return redirect('/notes/user')

