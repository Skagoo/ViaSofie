# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-11 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0019_auto_20170411_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='pand',
            name='beschrijving_2',
            field=models.TextField(blank=True, null=True),
        ),
    ]
