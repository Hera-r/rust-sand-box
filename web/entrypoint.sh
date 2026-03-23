#!/bin/bash
set -e

echo "Creating migrations..."
python manage.py makemigrations core --noinput

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput 2>/dev/null || true

echo "Seeding exercises..."
python manage.py seed_exercises

echo "Starting server..."
exec python manage.py runserver 0.0.0.0:8000
