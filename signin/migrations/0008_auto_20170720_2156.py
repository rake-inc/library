# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-07-20 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0007_auto_20170718_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]