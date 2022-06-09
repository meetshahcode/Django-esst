from django import forms
from .models import Note


class NoteForm(forms.Form):
    """NoteForm definition."""
    class meta:
        model = Note
        fields = ('Title','notes')

    def clean_Title(self):
        Title = self.cleaned_data.get('Title')
        if 'Django' not in Title:
            raise
        return Title

