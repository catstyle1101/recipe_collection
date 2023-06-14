#!/bin/sh
python manage.py migrate;
python manage.py collectstatic --noinput;
python manage.py filldatabase
gunicorn -w 2 -b 0:8000 foodgram_backend.wsgi;