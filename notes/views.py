from datetime import datetime

from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, TemplateView

from notes.models import Note


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


def note_add(request):
    note = Note()
    note.user = request.user
    note.title = request.POST['title']
    note.content = request.POST['content']
    note.created = datetime.now()
    note.save()
    return redirect('/notes/user')

