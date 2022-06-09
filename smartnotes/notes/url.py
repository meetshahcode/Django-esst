from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.NoteListView.as_view(),name = 'notes.list'),    
    path('list/<int:pk>',views.NoteDetailView.as_view(),name = 'notes.detail'),  
    path('list/new/',views.NoteCreateView.as_view(),name = 'notes.new'),
    path('list/<int:pk>/update/',views.NoteUpdateView.as_view() ,name = 'notes.update'),   
    path('list/<int:pk>/remove/',views.NoteDeleteView.as_view() ,name = 'notes.remove')    
]