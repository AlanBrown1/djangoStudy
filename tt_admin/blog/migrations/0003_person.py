# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170323_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='名')),
                ('last_name', models.CharField(max_length=30, verbose_name='姓')),
            ],
        ),
    ]
