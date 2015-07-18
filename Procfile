web: gunicorn mysite.wsgi --log-file -
scheduler: python manage.py celery worker -B -E --maxtasksperchild=1000


