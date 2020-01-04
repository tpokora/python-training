from django.urls import path

from . import views

app_name = "notes"
urlpatterns = [
    path('user', views.UserNotesView.as_view(), name='user_notes'),
    path('add', views.note_add, name='note_add'),
    path('delete/<int:note_id>', views.note_delete, name='note_delete')
]
