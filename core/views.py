# Create your views here.
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView

from core.models import User, UserConfiguration
from notes.utils import NoteUtils


class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        NoteUtils.context_add_user_past_due_notes(context, self.request)
        return context


class UsersListView(ListView):
    template_name = 'home/users.html'
    model = User
    context_object_name = 'users'
    queryset = User.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        NoteUtils.context_add_user_past_due_notes(context, self.request)
        return context


class UserDetailsView(DetailView):
    template_name = 'home/user.html'
    model = User

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        NoteUtils.context_add_user_past_due_notes(context, self.request)
        return context

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')
        return super().get(self, request, *args, **kwargs)


class UserConfigurationView(TemplateView):
    template_name = 'home/user_configuration.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        NoteUtils.context_add_user_past_due_notes(context, self.request)
        return context

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')
        return super().get(self, request, *args, **kwargs)
