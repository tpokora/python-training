from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from django.urls import path

from training import settings
from . import views

app_name = "core"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home', views.IndexView.as_view(), name='index'),
    path('users', views.UsersListView.as_view(), name='users'),
    path('user/<int:pk>', views.UserDetailsView.as_view(), name='user'),
    path('user/configuration', views.UserConfigurationView.as_view(), name='user_configuration'),
    url(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout')
]