from django.db import models


class TaskLog(models.Model):
    taskid = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)