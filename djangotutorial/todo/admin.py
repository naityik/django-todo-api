from django.contrib import admin

# Register your models here.
from .models import Task # Import your model

admin.site.register(Task) # Tell the admin to show it