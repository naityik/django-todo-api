from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'completed', 'user']
        # We make the user field read-only so users can't 'assign' tasks to others
        read_only_fields = ['user']