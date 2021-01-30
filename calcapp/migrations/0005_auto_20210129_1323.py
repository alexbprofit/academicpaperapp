# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-29 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calcapp', '0004_auto_20210129_0759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result1', models.FloatField()),
                ('result2', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
