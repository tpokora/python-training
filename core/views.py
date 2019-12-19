# Create your views here.
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, DetailView


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
    context_object_name = 'users'
    queryset = User.objects.all()


class UserDetailsView(DetailView):
    template_name = 'home/user.html'
    model = User
