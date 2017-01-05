# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_auto_20170102_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='plan_time',
            field=models.CharField(blank=True, choices=[('allday', 'All day'), ('midnight', 'Midnight'), ('dawn', 'Dawn'), ('morning', 'Morning'), ('noon', ' Noon'), ('afternoon', 'Afternoon'), ('dust', 'Dust'), ('evening', 'Evening')], max_length=9, null=True),
        ),
    ]