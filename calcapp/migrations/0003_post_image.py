# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-29 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calcapp', '0002_post_nums'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=5, upload_to='plot.png'),
            preserve_default=False,
        ),
    ]