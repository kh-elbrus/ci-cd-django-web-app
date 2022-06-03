#!/bin/bash

set -xe

python manage.py migrate --noinput

python manage.py collectstatic --noinput --clear

gunicorn app.wsgi:application --reload -w 3 -b 0.0.0.0:8000
