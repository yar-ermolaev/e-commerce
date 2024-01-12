#!/bin/sh
until cd /app/store
do
  echo "Waiting for server..."
done

cd ..

celery -A store worker -l info
