from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

from notes.models import Note


class NoteForm(forms.Form):
    title = forms.CharField(max_length=50, min_length=5)
    content = forms.CharField(max_length=300)


def note_add(request):
    submitted = False
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note_data = form.cleaned_data
            note = Note.fill(note_data, request.user)
            note.save()
            return HttpResponseRedirect('/notes/user?submitted=True')
        else:
            form = NoteForm()
            if 'submitted' in request.GET:
                submitted = True

        return render(request, 'notes/user_notes.html', {'form': form, 'submitted': submitted})
