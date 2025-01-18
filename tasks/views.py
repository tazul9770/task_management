from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task, TaskDetail, Project
from django.contrib import messages
from datetime import date
from django.db.models import Q, Count, Max, Min, Avg


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

    # # retrive all data form task
    # tasks = Task.objects.all()
    # #retrive a specific task
    # task3 = Task.objects.get(id = 3)
    # #fetch the first task
    # first_task = Task.objects.first()

    #show task that are completed
    # tasks = Task.objects.filter(status = "COMPLETED") 

    #show the task which due date is today
    # tasks = Task.objects.filter(due_date = date.today())

    # show the task whose priority is not low
    # tasks = TaskDetail.objects.exclude(priority = "L")

    # show the task that contain the word 'paper' and status pending
    #tasks = Task.objects.filter(title__icontains = "c", status = "PENDING")

    #show the task which are pending or in-progress
    #tasks = Task.objects.filter(Q(status = "PENDING") | Q(status = "IN_PROGRESS"))

    # select related (foreignKey er jonno ek dike sodo khatbe, oneToOneKey er jonno 2 dikei)
    #tasks = Task.objects.select_related('details').all() 
    #tasks = TaskDetail.objects.select_related('task').all()
    #tasks = Task.objects.select_related('project').all()

    #prefetch related(reverse foreign key er jonno kaj kore r manyToMnay er jonno kore)
    #tasks = Project.objects.prefetch_related('task_set').all()
    #tasks = Task.objects.prefetch_related('assigned_to').all()

    #Aggregate function
    #task_count = Task.objects.aggregate(num_task = Count('id'))
    task_count = Project.objects.annotate(num_task = Count('task')).order_by('num_task')
    return render(request, "show_task.html", {"task_count":task_count})



