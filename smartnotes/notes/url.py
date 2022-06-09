from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.NoteListView.as_view(),name = 'notes.list'),    
    path('list/<int:pk>',views.NoteDetailView.as_view(),name = 'notes.detail'),  
    path('list/new/',views.NoteCreateView.as_view(),name = 'notes.new')    
]