from django.urls import path
from tasks.views import manager_dashboard, employee_dashboard, create_task, view_task, update_task, delete_task, task_details, dashboard, Greetings, HiGreetings, CreateTask, ViewProject, TaskDetail, UpdateTask

urlpatterns = [
    path('manager-dashboard/', manager_dashboard, name="manager-dashboard"),
    path('user-dashboard/', employee_dashboard, name='user-dashboard'),
    #path('create-task/', create_task, name='create-task'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    #path('view_task/', view_task, name='view-task'),
    path('view_task/', ViewProject.as_view(), name='view-task'),
    #path('task/<int:task_id>/details/', task_details, name='task-details'),
    path('task/<int:pk>/details/', TaskDetail.as_view(), name='task-details'),
    #path('update-task/<int:id>/', update_task, name='update-task'),
    path('update-task/<int:id>/', UpdateTask.as_view(), name='update-task'),
    path('delete-task/<int:id>/', delete_task, name='delete-task'),
    path('dashboard', dashboard, name='dashboard'),
    path('greetings/', HiGreetings.as_view(greetings = "mastani korlam"), name='greetings')
]