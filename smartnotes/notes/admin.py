from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Note)
class NotesAdmin(admin.ModelAdmin):
    list_display = ["Title","id","created_on"]