# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 08:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Category'),
        ),
    ]