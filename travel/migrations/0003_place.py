# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_auto_20170102_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=196)),
                ('name', models.CharField(max_length=196)),
                ('icon', models.URLField(blank=True, null=True)),
                ('address', models.TextField()),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('plan_date', models.DateField()),
                ('plan_time', models.CharField(blank=True, choices=[('allday', 'All day'), ('midnight', 'Midnight'), ('dawn', 'Dawn'), ('morning', 'Morning'), ('noon', ' Noon'), ('afternoon', 'Afternoon'), ('dust', 'Dust'), ('evening', 'Evening')], max_length=9, null=True)),
                ('added_at', models.DateTimeField()),
                ('sort', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
            ],
            options={
                'ordering': ['sort'],
            },
        ),
    ]
