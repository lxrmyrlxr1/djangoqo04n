#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn dj2.wsgi:application --bind 0.0.0.0:$PORT

