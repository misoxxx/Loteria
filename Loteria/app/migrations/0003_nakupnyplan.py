# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160520_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='NakupnyPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cena', models.IntegerField()),
                ('pocetTiketov', models.IntegerField()),
                ('text', models.CharField(max_length=200)),
            ],
        ),
    ]
