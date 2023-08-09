from django.contrib import admin
from .models import Task, TaskHistory, Service

admin.site.register(TaskHistory)
admin.site.register(Task)
admin.site.register(Service)
