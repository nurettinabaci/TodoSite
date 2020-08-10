from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
# Create your views here.
from .models import *
from .forms import TaskForm, CreateUserForm
from .decorators import unauthenticated_user, authenticated_user

@authenticated_user
def mainPage(request):
    tasks = Task.objects.filter(user=request.user.enduser)
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user.enduser
            form.save()
            return redirect('/')


    context = {'tasks': tasks[::-1], 'form':form}
    return render(request, 'tasks/todoList.html', context)


@authenticated_user
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


@authenticated_user
def deleteTask(request,pk):
    task = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task':task}

    return render(request, 'tasks/delete_task.html', context)

@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request,user)
			return redirect('todoList')
		else:
			messages.info(request, 'Username or password incorrect!')

	context = {}
	return render(request, 'tasks/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')

@unauthenticated_user
def register(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'You successfuly created an account for {username}.')
			return redirect('login')
	context = {'form':form}
	return render(request, 'tasks/register.html', context)