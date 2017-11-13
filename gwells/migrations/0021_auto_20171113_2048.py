# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-13 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0020_auto_20171113_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peforation',
            fields=[
                ('who_created', models.CharField(max_length=30)),
                ('when_created', models.DateTimeField(blank=True, null=True)),
                ('who_updated', models.CharField(max_length=30, null=True)),
                ('when_updated', models.DateTimeField(blank=True, null=True)),
                ('perforation_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('liner_thickness', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True, verbose_name='Liner Thickness')),
                ('liner_diameter', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Liner Diameter')),
                ('liner_from', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Liner From')),
                ('liner_to', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Liner To')),
                ('liner_perforation_from', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Perforation From')),
                ('liner_perforation_to', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Perforation To')),
                ('well_tag_number', models.ForeignKey(blank=True, db_column='well_tag_number', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.Well')),
            ],
            options={
                'ordering': ['perforation_guid'],
                'db_table': 'gwells_perforation',
            },
        ),
        migrations.RenameField(
            model_name='activitysubmission',
            old_name='well',
            new_name='well_tag_number',
        ),
    ]
