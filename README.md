LUNCH SCHEDULER
-----------------------------------
This network site is a quick sketch 

It uses a list representation of the people and their connections.
I.e. for each person, they are connected to other people in the list. 

While this may not be computationally effective, it is good enough 
for a small amount of people. :) 

PURPOSE:
Automatically choose aquaintences to eat food with eachother.  

TECHNOLOGY: 
Celery

Nice-to-haves:
OAuth authentication with Facebook (see pictures)
Email notification


HOW TO START CELERY!!
redis-server \\ startup the server
python manage.py celery worker -E \\ startup the worker, alternatively, 
                \\python manage.py celery worker --loglevel=info
celery -A mysite beat \\ this starts the celery beat for periodic tasks

\\ YAY CELERY!!!
python manage.py celery worker --beat
