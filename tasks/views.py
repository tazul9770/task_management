from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("welcome to the task management system!")

def contact(request):
    return HttpResponse("<h1 style = 'color: green'>This is contact page</h1>")

def show_task(request):
    return HttpResponse("This is a task page")
