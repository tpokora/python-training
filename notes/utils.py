from notes.models import NoteQuerySet


class NoteUtils():

    @staticmethod
    def context_add_user_past_due_notes(context, request):
        if request.user.is_authenticated:
            context['notes_due_quantity'] = len(NoteQuerySet.get_user_past_due_notes(request.user).all())
