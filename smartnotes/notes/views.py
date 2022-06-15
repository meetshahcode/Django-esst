from django.shortcuts import render
from .models import Note
from .forms import NoteForm
from django.http import Http404,HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class NoteDeleteView(DeleteView):
    model = Note
    success_url = "/smart/list"


class NoteUpdateView(UpdateView):
    model = Note
    success_url = "/smart/list"
    form_class = NoteForm

class NoteCreateView(CreateView):
    model = Note
    success_url = "/smart/list"
    form_class = NoteForm

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NoteListView(LoginRequiredMixin ,ListView):
    model = Note
    context_object_name = "Notes"
    template_name = "notes/note_list.html"
    login_url = "login"
    def get_queryset(self):
        return self.request.user.note.all()


class NoteDetailView(DetailView):
    model = Note
    context_object_name = "note"
