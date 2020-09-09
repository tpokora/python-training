# Create your views here.
from django.contrib.auth.models import User, Group
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from rest_framework import viewsets

from core.serializers import UserSerializer, GroupSerializer


class IndexView(TemplateView):
    template_name = 'home/index.html'

    message = 'Hello World'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = self.message
        return context


# Rest endpoint
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
