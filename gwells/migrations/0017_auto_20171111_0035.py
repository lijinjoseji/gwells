# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-11 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0016_auto_20171109_2349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surfacesealmaterial',
            old_name='code',
            new_name='surface_seal_material_code',
        ),
        migrations.RenameField(
            model_name='surfacesealmethod',
            old_name='code',
            new_name='surface_seal_method_code',
        ),
        migrations.RemoveField(
            model_name='well',
            name='surface_seal_depth',
        ),
        migrations.AddField(
            model_name='well',
            name='surface_seal_length',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Surface Seal Length'),
        ),
    ]
