from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Task
from .forms import TaskForm



def mainPage(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save() # saves to database
        return redirect('/')

    context = {'tasks': tasks[::-1], 'form':form}

    return render(request, 'tasks/todoList.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method=='POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request,pk):
    task = Task.objects.get(id=pk)
    
    
    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task':task}

    return render(request, 'tasks/delete_task.html', context)
