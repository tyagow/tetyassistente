from __future__ import absolute_import, unicode_literals
from celery.task import task


@task()
def verify_user(self):
    print('user')