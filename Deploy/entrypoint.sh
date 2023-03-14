#!/bin/bash

python manage.py migrate --no-input

supervisord -c /opt/app/Deploy/supervisor.conf
