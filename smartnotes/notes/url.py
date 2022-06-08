from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.list,name = 'list'),    
    path('list/<int:pk>',views.details,name = 'details')    
]