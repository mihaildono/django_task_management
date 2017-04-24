# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-20 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import todo.models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0014_auto_20170418_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=todo.models.user_directory_path),
        ),
    ]