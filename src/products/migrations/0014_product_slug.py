# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_remove_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True,blank=True, null=True),
            preserve_default=False, 
        ),
    ]
