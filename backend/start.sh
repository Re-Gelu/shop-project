#!/bin/sh

python manage.py createcachetable
python manage.py migrate --noinput
python manage.py collectstatic --no-input --clear
gunicorn config.wsgi:application --bind 0.0.0.0:8000