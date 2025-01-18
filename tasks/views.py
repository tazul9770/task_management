from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task
from django.contrib import messages

def manager_dashboard(request):
    return render(request, "dashboard/admin.html")

def user_dashboard(request):
    return render(request, "dashboard/user.html")

def test(request):
    context = {
        "names":["rahim", "karim", "shakib", "tamim"]
    }
    return render(request, "test.html", context)

def create_task(request):
    #employees = Employee.objects.all()
    form = TaskModelForm() # by defaul for get
    if request.method == "POST":
         form  = TaskModelForm(request.POST)
         if form.is_valid():
             '''for model form data'''
             form.save()
             
             #return render(request, 'task_form.html', {"form":form}, {"messege": "Task added successfully"})

    context = {"form":form}
    return render(request, "task_form.html", context)

def view_task(request):
    # retrive all data form task
    tasks = Task.objects.all()
    #retrive a specific task
    task3 = Task.objects.get(id = 3)
    #fetch the first task
    first_task = Task.objects.first()
    return render(request, "show_task.html", {"tasks":tasks, "task3":task3, "first_task":first_task})



