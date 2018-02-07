#!/bin/bash

cd $TRAVIS_BUILD_DIR/src/backend
python manage.py collectstatic --noinput --settings=conf.staging
