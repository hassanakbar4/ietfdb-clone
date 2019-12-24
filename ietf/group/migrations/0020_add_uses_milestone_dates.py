# Copyright The IETF Trust 2019, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-30 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0019_rename_field_document2'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='uses_milestone_dates',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='grouphistory',
            name='uses_milestone_dates',
            field=models.BooleanField(default=False),
        ),
    ]
