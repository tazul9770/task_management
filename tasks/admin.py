from django.contrib import admin
from tasks.models import Task, TaskDetail, Employee, Project

admin.site.register(Task)
admin.site.register(TaskDetail)
admin.site.register(Employee)
admin.site.register(Project)
