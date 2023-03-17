#!/bin/bash

if [ "$PG_DATABASE_NAME" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z db 5432; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py migrate --no-input
python manage.py collectstatic --no-input

supervisord -c /opt/app/Deploy/supervisor.conf
