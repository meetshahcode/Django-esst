from django.shortcuts import render
from . import models
from django.http import Http404
# Create your views here.

def list(request):
    all_notes = models.Note.objects.all()
    return render(request, "notes/notes_list.html",{'Notes':all_notes})

def details(request,pk):
    try:
        note_obj = models.Note.objects.get(pk=pk)
    except models.Note.DoesNotExist:
        raise Http404("Note doesn't exist.")
    return render(request,"notes/notes_details.html",{'note':note_obj})