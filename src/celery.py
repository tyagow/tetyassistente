from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

import django
django.setup()

app = Celery('tety')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    pass
    # Calls test('hello') every 10 seconds.
    # sender.add_periodic_task(10.0, 'src.core.tasks.test',kwargs='1', name='add every 10')
    #
    # # Calls test('world') every 30 seconds
    # sender.add_periodic_task(30.0, test.s({'id': '1'}), name='every 30')

