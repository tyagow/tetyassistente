from django.contrib import admin

# Register your models here.
from src.core.models import TaskLog

admin.site.register(TaskLog)