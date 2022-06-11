from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    Title = models.CharField(max_length=200)
    notes = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="note")
    def __str__(self):
        return self.Title
