from django.shortcuts import render, redirect
from django.urls import reverse
from . forms import ToDoForm
from . models import ToDo
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/signup/')
@permission_classes([IsAuthenticated])
def todo_list(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect(reverse('todo:todo_list'))
    else:
        form = ToDoForm()

    todos = ToDo.objects.filter(user = request.user)
    return render(request, 'todo/todo_list.html', {
    'todos': todos,
    'form': form
})

@permission_classes([IsAuthenticated])
def delete_todo(request,id):
    todo = ToDo.objects.get( id = id )
    todo.delete()
    return redirect('todo:todo_list')

@permission_classes([IsAuthenticated])
def todo_check(request,id):
    if request.method == 'POST':
        todo = get_object_or_404(ToDo,id=id,user=request.user)
        todo.is_done = not todo.is_done
        todo.save()
        return JsonResponse({'success':True,'is_done':todo.is_done})
    return JsonResponse({'success':False}, status =400)

@permission_classes([IsAuthenticated])
def edit_todo(request, id):
    todo = get_object_or_404(ToDo, id=id, user=request.user)

    if request.method == 'POST':
        edit_form = ToDoForm(request.POST, instance=todo)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('todo:todo_list')
    else:
        edit_form = ToDoForm(instance=todo)

    return render(request, 'todo/todo_list.html', {
        'form': edit_form,
        'todos': ToDo.objects.filter(user=request.user)
    })





