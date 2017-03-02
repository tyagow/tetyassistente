from __future__ import absolute_import, unicode_literals

from celery import Celery
from celery.schedules import crontab

from src.core.models import TaskLog

app = Celery('tety')
#
# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, test.s('1'))
#

@app.task(name='testtask')
def test(self, **kwargs):
    tasklog, created = TaskLog.objects.get_or_create(taskid=self)
    print('kwargs %s' % self)
    tasklog.save()

# app.add_periodic_task(crontab(hour=0, minute=1), test.s())