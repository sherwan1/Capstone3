# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-07 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0009_auto_20171226_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default=b'pic_folder/no-img.jpg', upload_to=b'pic_folder/'),
        ),
    ]
