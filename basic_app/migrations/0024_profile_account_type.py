# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-20 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0023_auto_20180219_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account_type',
            field=models.CharField(max_length=150, null=True),
        ),
    ]