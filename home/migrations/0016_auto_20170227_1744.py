# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-27 06:44
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20170227_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('content_width', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default=12, max_length=2)),
                ('content_offset', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default=0, max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='page',
            name='content',
        ),
        migrations.RemoveField(
            model_name='page',
            name='content_width',
        ),
    ]
