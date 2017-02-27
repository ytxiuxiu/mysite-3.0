# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-27 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_page_cover_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['sort']},
        ),
        migrations.AddField(
            model_name='link',
            name='sort',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
    ]