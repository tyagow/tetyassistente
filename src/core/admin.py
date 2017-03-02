from django.contrib import admin

# Register your models here.
from src.core.models import TaskLog


class TaskLogAdmin(admin.ModelAdmin):

    readonly_fields = ['timestamp', 'updated']
    list_display = ['taskid', 'timestamp', 'updated']


admin.site.register(TaskLog, TaskLogAdmin)