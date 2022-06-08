from django.db import models

# Create your models here.

class Note(models.Model):
    Title = models.CharField(max_length=200)
    notes = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Title
