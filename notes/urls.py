from django.urls import path

from . import views

app_name = "notes"
urlpatterns = [
    path('user', views.UserNotesView.as_view(), name='user_notes')
]
