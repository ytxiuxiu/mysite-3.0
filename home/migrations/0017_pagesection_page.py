# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-27 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20170227_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagesection',
            name='page',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Page'),
            preserve_default=False,
        ),
    ]
