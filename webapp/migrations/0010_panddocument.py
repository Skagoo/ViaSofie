# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-30 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_pandepc'),
    ]

    operations = [
        migrations.CreateModel(
            name='PandDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(blank=True, upload_to=b'documents/%Y/%m/%d')),
                ('naam', models.CharField(max_length=256)),
                ('pand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Pand')),
            ],
        ),
    ]