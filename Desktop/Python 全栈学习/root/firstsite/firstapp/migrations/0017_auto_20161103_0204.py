# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 02:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0016_auto_20161102_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2016, 11, 3, 2, 4, 29, 298752)),
        ),
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.CharField(blank=True, choices=[('大学生', '大学生'), ('老年人', '老年人'), ('信用卡', '信用卡'), ('扫二维码', '扫二维码'), ('短信', '短信')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateField(default=datetime.datetime(2016, 11, 3, 2, 4, 29, 299928)),
        ),
    ]
