# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import migrations
from django.contrib.auth.admin import User


def create_superuser(apps, schema_editor):
    superuser = User()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.username = 'admin'
    superuser.email = 'admin@admin.net'
    superuser.set_password('qazqaz123')
    superuser.date_joined = datetime.now()
    superuser.last_login = datetime.now()
    superuser.last_name = ''
    superuser.first_name = ''
    superuser.save()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180205_1849'),
    ]

    operations = [
        migrations.RunPython(create_superuser)
    ]
