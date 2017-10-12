# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 12:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0008_auto_20170927_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preaching',
            name='pr_title',
        ),
        migrations.AddField(
            model_name='preaching',
            name='series_title',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='podcast.Series'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='preaching',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]