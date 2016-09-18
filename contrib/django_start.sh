#!/bin/bash
/usr/local/bin/python /wttd/manage.py test
/usr/local/bin/python /wttd/manage.py migrate
/usr/local/bin/python /wttd/manage.py runserver 0.0.0.0:8000
