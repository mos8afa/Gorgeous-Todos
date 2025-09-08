from django.urls import path
from . views import todo_list,delete_todo,todo_check,edit_todo
from .api_view import ToDoListApi, ToDoEditAndDeleteApi

app_name = 'todo'

urlpatterns = [
    path('',todo_list,name='todo_list'),
    path('delete/<int:id>/',delete_todo,name='delete_todo'),
    path('check/<int:id>/',todo_check,name='todo_check'),
    path('edit/<int:id>/', edit_todo, name='edit_todo'),


    path('todo_list/api/', ToDoListApi.as_view(), name='todo_list_api' ),
    path('todo_detail/api/<int:id>',ToDoEditAndDeleteApi.as_view(),name='todo_detail'),
]
