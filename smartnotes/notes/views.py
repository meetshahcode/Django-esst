from django.shortcuts import render
from .models import Note
from .forms import NoteForm
from django.http import Http404
from django.views.generic import ListView,DetailView,CreateView
# Create your views here.


class NoteCreateView(CreateView):
    model = Note
    fields = ["Title","notes"]
    success_url = "/smart/list"
    form_class = NoteForm

class NoteListView(ListView):
    model = Note
    context_object_name = "Notes"
    template_name = "notes/note_list.html"


class NoteDetailView(DetailView):
    model = Note
    context_object_name = "note"
