# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-09 20:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_jobopportunity_availability'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobopportunity',
            old_name='availability',
            new_name='available',
        ),
    ]
