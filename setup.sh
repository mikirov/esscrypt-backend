#!/bin/bash

# Load environment variables from .env
if [ -f .env ]; then
    export $(cat .env | xargs)
fi

# Install project dependencies from requirements.txt
pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi