from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views # Import the whole views file

router = DefaultRouter()
# This creates routes for: list, create, retrieve, update, and delete
router.register(r'tasks-api', views.TaskViewSet, basename='task-api')

urlpatterns = [
    # HTML Website Routes
    path('', views.task_list, name='task_list'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('toggle/<int:pk>/', views.toggle_task, name='toggle_task'),
    path('register/', views.register, name='register'),

    # API Routes (JSON)
    path('api/', include(router.urls)), 
]