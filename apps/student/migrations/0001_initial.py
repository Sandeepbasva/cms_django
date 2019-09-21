# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-31 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sid', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=20)),
                ('course', models.CharField(choices=[('B.Tech', 'B.tech')], default='B.Tech', max_length=20)),
                ('year', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=32)),
            ],
        ),
    ]