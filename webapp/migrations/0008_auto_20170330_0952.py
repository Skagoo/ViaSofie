# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-30 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20170330_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]