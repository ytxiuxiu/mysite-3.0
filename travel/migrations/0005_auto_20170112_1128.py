# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_auto_20170111_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.DecimalField(decimal_places=14, max_digits=17),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.DecimalField(decimal_places=14, max_digits=17),
        ),
    ]
