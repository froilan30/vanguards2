# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 09:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0004_auto_20170927_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preaching',
            name='created',
        ),
        migrations.RemoveField(
            model_name='series',
            name='created',
        ),
    ]