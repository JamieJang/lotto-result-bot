# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResultNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rounds', models.CharField(max_length=1024)),
                ('result', models.CharField(max_length=1024)),
            ],
            options={
                'ordering': ['rounds'],
            },
        ),
    ]
