#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn tourism_system.wsgi:application --bind 0.0.0.0:$PORT
