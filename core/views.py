# Create your views here.
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView


class IndexView(TemplateView):
    template_name = 'home/index.html'

    message = 'Hello World'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = self.message
        return context


class UsersListView(ListView):
    template_name = 'home/users.html'
    model = User

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context
