from django.contrib import admin
from .models import ToDo
from django_summernote.admin import SummernoteModelAdmin

class SomeModelAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'
    list_display = ['name','price_per_day']

admin.site.register(ToDo)

