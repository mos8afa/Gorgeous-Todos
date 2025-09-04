from django.contrib import admin
from .models import ToDo
from django_summernote.admin import SummernoteModelAdmin

class ToDoAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'
    list_display = ['name','created_at','is_done']

admin.site.register(ToDo,ToDoAdmin)

