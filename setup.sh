#!/bin/bash

# Load environment variables from .env
if [ -f .env ]; then
    export $(cat .env | xargs)
fi

# Install project dependencies from requirements.txt
pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput

# Create a superuser
python3.9 manage.py createsuperuser --username "$DJANGO_ADMIN_USERNAME" --password "$DJANGO_SUPERUSER_PASSWORD"
