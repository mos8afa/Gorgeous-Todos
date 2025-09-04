from django.urls import path
from . views import todo_list,delete_todo

app_name = 'todo'

urlpatterns = [
    path('',todo_list,name='todo_list'),
    path('delete/<int:id>/',delete_todo,name='delete_todo')
]
