# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-15 22:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0029_auto_20171115_2206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productiondata',
            old_name='well_guid',
            new_name='well',
        ),
    ]
