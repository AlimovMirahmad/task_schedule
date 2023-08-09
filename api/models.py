from django.db import models
import uuid
import time

HTTP_METHODS = (
    (1, 'GET'),
    (2, 'POST')
)

TASK_STATUSES = (
    (1, 'ACTIVE'),
    (2, 'BLOCK')
)


class Service(models.Model):
    service_name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    service_secret = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.service_name


class Task(models.Model):
    task_description = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    request_url = models.URLField()
    request_type = models.IntegerField(choices=HTTP_METHODS, default=1)
    request_body = models.JSONField(blank=True, null=True)

    datatime = models.TextField(null=True, blank=True)

    task_status = models.IntegerField(choices=TASK_STATUSES, default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_description


class TaskHistory(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    response = models.TextField(blank=True, null=True)
    status = models.IntegerField(default=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task.task_description
