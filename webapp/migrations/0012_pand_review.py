# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-01 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_pand_plattegrond'),
    ]

    operations = [
        migrations.AddField(
            model_name='pand',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
    ]
