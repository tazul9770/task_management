from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm, TaskDetailModelForm
from tasks.models import Employee, Task, TaskDetail, Project
from django.contrib import messages
from datetime import date
from django.db.models import Q, Count, Max, Min, Avg


def manager_dashboard(request):
    type = request.GET.get('type', 'all')

    counts = Task.objects.aggregate(
        total = Count('id'),
        completed = Count('id', filter = Q(status = "COMPLETED")),
        in_progress = Count('id', filter = Q(status = "IN_PROGRESS")),
        pending = Count('id', filter = Q(status = "PENDING"))
        )
    
    # retriving task data
    base_query = Task.objects.select_related('details').prefetch_related('assigned_to')

    if type == 'completed':
        tasks = base_query.filter(status = "COMPLETED")
    elif type == 'in_progress':
        tasks = base_query.filter(status = "IN_PROGRESS")
    elif type == 'pending':
        tasks = base_query.filter(status = "PENDING")
    elif type == 'all':
        tasks = base_query.all()

    context = {
        "tasks":tasks,
        "counts":counts
    }

    return render(request, "dashboard/admin.html", context)

def user_dashboard(request):
    return render(request, "dashboard/user.html")

def test(request):
    context = {
        "names":["rahim", "karim", "shakib", "tamim"]
    }
    return render(request, "test.html", context)

def create_task(request):
    #employees = Employee.objects.all()
    task_form = TaskModelForm() # by defaul for get
    task_detail_form = TaskDetailModelForm()

    if request.method == "POST":
         task_form = TaskModelForm(request.POST) 
         task_detail_form = TaskDetailModelForm(request.POST)
         if task_form.is_valid() and task_detail_form.is_valid():
             '''for model form data'''
             task = task_form.save()
             task_detail = task_detail_form.save(commit=False)
             task_detail.task = task
             task_detail.save()
             
             messages.success(request, "Task created successfully")
             return redirect('create_task')

    context = {"task_form":task_form, "task_detail_form":task_detail_form}
    return render(request, "task_form.html", context)

def update_task(request, id):
    task = Task.objects.get(id=id)
    task_form = TaskModelForm(instance = task) # by defaul for get
    
    if task.details:
        task_detail_form = TaskDetailModelForm(instance = task.details)

    if request.method == "POST":
         task_form = TaskModelForm(request.POST, instance = task) 
         task_detail_form = TaskDetailModelForm(request.POST, instance = task.details)
         if task_form.is_valid() and task_detail_form.is_valid():
             '''for model form data'''
             task = task_form.save()
             task_detail = task_detail_form.save(commit=False)
             task_detail.task = task
             task_detail.save()
             
             messages.success(request, "Task updated successfully")
             return redirect('update_task', id)

    context = {"task_form":task_form, "task_detail_form":task_detail_form}
    return render(request, "task_form.html", context)

def delete_task(request, id):
    if request.method == "POST":
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request, "Task deleted successfully")
        return redirect('manager_dashboard')
    else:
        messages.error(request, "Something wrong!")
        return redirect('manager_dashboard')
    

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

    # show the task whose priority is not low/low chara sobai k dekhaba
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



