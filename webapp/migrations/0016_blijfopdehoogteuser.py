# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-11 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_delete_pandreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlijfOpDeHoogteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voornaam', models.CharField(max_length=128)),
                ('naam', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128, unique=True)),
                ('telefoonnummer', models.CharField(max_length=128, unique=True)),
                ('straatnaam', models.CharField(max_length=128)),
                ('huisnr', models.CharField(max_length=10)),
                ('plaats', models.CharField(blank=True, max_length=10, null=True)),
                ('postcode', models.CharField(max_length=50)),
                ('min_price', models.IntegerField(default=0)),
                ('max_price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
