# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-05 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0014_auto_20170205_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelconstraint',
            name='time',
            field=models.TimeField(),
        ),
    ]
