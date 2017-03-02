web: uwsgi uwsgi.ini
worker: celery -A src worker -l info
beat:  celery -A src beat -l info -S django