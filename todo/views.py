from django.shortcuts import render, redirect
from . models import ToDo

def todo_list(request):
    todos = ToDo.objects.filter(user = request.user)
    return render(request,'todo/todo_list.html',{'todos':todos})

def delete_todo(request,id):
    todo = ToDo.objects.get( id = id )
    todo.delete()
    return redirect('todo/todo_list')