from django.contrib import admin
from django.urls import path 
from taskplannerapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.sprint_list, name='sprint_list'),
    path('sprints/add/', views.add_sprint, name='add_sprint'),
    path('sprints/<int:sprint_id>/tasks/', views.task_list, name='task_list'),
    path('sprints/<int:sprint_id>/tasks/add/', views.add_task, name='add_task'),
    path('tasks/<int:task_id>/update/', views.update_task, name='update_task'),
    path('users/<int:user_id>/tasks/', views.user_tasks, name='user_tasks'),
    path('sprints/<int:sprint_id>/ai-suggestions/', views.ai_suggestions, name='ai_suggestions'),
]