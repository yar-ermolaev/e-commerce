#!/bin/sh
until cd /app/store
do
  echo "Waiting for server..."
done

cd ..

until python manage.py migrate
do
  echo "Waiting for db to be ready..."
  sleep 2
done

python manage.py runserver 0.0.0.0:8000
