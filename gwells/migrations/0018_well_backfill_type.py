# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-13 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0017_auto_20171111_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='well',
            name='backfill_type',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Backfill Type'),
        ),
    ]
