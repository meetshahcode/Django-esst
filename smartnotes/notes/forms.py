from django import forms
from .models import Note
from django.core.exceptions import ValidationError

class NoteForm(forms.ModelForm):
    """NoteForm definition."""
    class Meta:
        model = Note
        fields = ['Title','notes']
        widgets = {
            'Title':forms.TextInput(attrs={"class":"form-control my-5"}),
            'notes':forms.Textarea(attrs={"class":"form-control my-5"})

        }
        labels = {
            'notes':'Write you thoughts'
        }
    
    def clean_Title(self):
        Title = self.cleaned_data['Title']
        if 'Django' not in Title:
            raise ValidationError("we only except note about Django")
        return Title
    
