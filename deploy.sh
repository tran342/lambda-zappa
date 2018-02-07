#!/bin/bash

cd $TRAVIS_BUILD_DIR/src/backend
zappa update dev
python manage.py collectstatic --noinput --settings=conf.staging
