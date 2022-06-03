#!/bin/bash

python manage.py collectstatic --noinput --clear

gunicorn --worker-tmp-dir /dev/shm blog.wsgi:application --reload -w 3 -b 0.0.0.0:8000
