from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('users', views.UsersListView.as_view(), name='users')
]