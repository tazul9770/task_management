from django.urls import path
from tasks.views import dashboard, CreateTask, ViewProject, TaskDetail, UpdateTask, ManagerDashboardView, EmployeeDashboard, TaskDeleteView

urlpatterns = [
    path('manager-dashboard/', ManagerDashboardView.as_view(), name='manager-dashboard'),
    path('user-dashboard/', EmployeeDashboard.as_view(), name='user-dashboard'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('view_task/', ViewProject.as_view(), name='view-task'),
    path('task/<int:pk>/details/', TaskDetail.as_view(), name='task-details'),
    path('update-task/<int:id>/', UpdateTask.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', TaskDeleteView.as_view(), name='delete-task'),
    path('dashboard/', dashboard, name='dashboard'),
]