# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20170321_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='format',
            field=models.CharField(choices=[('i', 'Digital'), ('d', 'DVD'), ('v', 'VHS')], default='i', max_length=1),
        ),
    ]