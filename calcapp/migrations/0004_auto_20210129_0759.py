# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-29 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calcapp', '0003_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='plot.png')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
