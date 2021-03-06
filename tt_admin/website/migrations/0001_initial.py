# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='书名')),
                ('author', models.CharField(max_length=30, verbose_name='作者')),
                ('pub_date', models.DateTimeField(verbose_name='出版时间')),
                ('price', models.IntegerField(verbose_name='价格')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30, verbose_name='品牌')),
                ('number', models.CharField(max_length=11, verbose_name='号码')),
                ('master', models.CharField(max_length=30, verbose_name='主人')),
                ('price', models.IntegerField(verbose_name='价格')),
            ],
        ),
    ]
