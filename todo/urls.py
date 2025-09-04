from django.urls import path
from . views import todo_list

app_name = 'todo'

urlpatterns = [
    path('',todo_list,name='todo_list')
]
