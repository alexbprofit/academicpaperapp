# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-28 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calcapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='nums',
            field=models.FloatField(default=4, max_length=10),
            preserve_default=False,
        ),
    ]
