# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-06 14:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='movieID',
        ),
    ]
