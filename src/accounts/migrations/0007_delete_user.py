# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-10 06:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_timestamp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
