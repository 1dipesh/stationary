# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='abc'),
            preserve_default=False,
        ),
    ]
