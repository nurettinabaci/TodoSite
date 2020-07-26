from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Task
from .forms import TaskForm, CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only


def mainPage(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
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


def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			messages.info(request, 'Username or password incorrect!')

	context = {}
	return render(request, 'tasks/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def register(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'You successfuly created an account for' + user)
			return redirect('login')
	context = {'form':form}
	return render(request, 'tasks/register.html', context)