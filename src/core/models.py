from django.db import models


class TaskLog(models.Model):
    task = models.ForeignKey('celery.task.PeriodicTask')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)