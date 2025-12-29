# from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task

class TaskTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_task_creation(self):
        # Create a task for that user
        task = Task.objects.create(title="Test Task", user=self.user)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.user.username, "testuser")