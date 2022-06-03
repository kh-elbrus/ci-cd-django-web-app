#!/bin/bash

set -xe

python manage.py migrate --noinput

python manage.py createsuperuser --email $DJANGO_SUPERUSER_EMAIL --noinput || true
