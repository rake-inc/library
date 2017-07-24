# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-07-18 18:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0005_auto_20170712_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=32, unique=True)),
                ('authorName', models.CharField(max_length=32)),
                ('numberOfBooks', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='book',
            name='detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signin.SignUp'),
        ),
    ]
