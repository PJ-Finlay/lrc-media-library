# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20170324_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='teacher_username',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]