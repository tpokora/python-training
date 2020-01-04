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

