# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('billing', 'Billing'), ('shipping', 'shipping')], default='shipping', max_length=120),
        ),
    ]