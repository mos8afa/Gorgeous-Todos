from django.shortcuts import render
from . models import ToDo

def todo_list(request):
    todos = ToDo.objects.filter(user = request.user)
    return render(request,'todo/todo_list.html',{'todos':todos})
