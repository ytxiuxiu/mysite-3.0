# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20161228_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groundfloortimber',
            name='name',
            field=models.CharField(blank=True, max_length=192, null=True),
        ),
    ]