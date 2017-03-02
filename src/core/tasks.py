from __future__ import absolute_import, unicode_literals

from celery.schedules import crontab
from celery.task import periodic_task

from src.core.models import TaskLog

from celery import app as celery_app


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('1'))


@celery_app.task
def test(self, **kwargs):
    tasklog = TaskLog.objects.get_or_create(taskid=self)
    tasklog.save()
    print('kwargs %s' % self)