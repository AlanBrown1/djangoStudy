# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 17:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(default=django.utils.timezone.now, max_length=3, verbose_name='状态'),
            preserve_default=False,
        ),
    ]
