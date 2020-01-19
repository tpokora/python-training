# Create your views here.
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView

from core.models import User
from notes.models import NoteQuerySet


class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            return context
        context['notes_due_quantity'] = len(NoteQuerySet.get_user_past_due_notes(self.request.user).all())
        return context


class UsersListView(ListView):
    template_name = 'home/users.html'
    model = User
    context_object_name = 'users'
    queryset = User.objects.all()


class UserDetailsView(DetailView):
    template_name = 'home/user.html'
    model = User

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')
        return super().get(self, request, *args, **kwargs)
