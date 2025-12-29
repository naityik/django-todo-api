from django.shortcuts import render, redirect # Add redirect
from .models import Task
from .forms import TaskForm # Import your form
from django.shortcuts import get_object_or_404 # Add this import
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login # To log the user in after they sign up
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer

@login_required(login_url='login')
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False) # Create the object but don't save to DB yet
            task.user = request.user       # Attach the logged-in user!
            task.save()                    # Now save it
            return redirect('task_list')

    return render(request, 'todo/index.html', {'tasks': tasks, 'form': form})

def delete_task(request, pk): #pk stands for primary key
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')

def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed # Switch True to False or vice versa
    task.save()
    return redirect('task_list')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Automatically log them in
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'todo/register.html', {'form': form})

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Again, ensure users only see THEIR tasks via the API
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically attach the user when creating via API
        serializer.save(user=self.request.user)