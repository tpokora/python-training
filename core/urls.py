from django.urls import path

from . import views

app_name = "core"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home', views.IndexView.as_view(), name='index'),
    path('users', views.UsersListView.as_view(), name='users'),
    path('user/<int:pk>', views.UserDetailsView.as_view(), name='user')
]