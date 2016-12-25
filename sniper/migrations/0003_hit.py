# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-25 01:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sniper', '0002_auto_20161223_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.TextField()),
                ('price', models.IntegerField()),
                ('url', models.URLField()),
                ('post_id', models.TextField()),
                ('date', models.DateTimeField()),
                ('sniper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sniper.CLSniper')),
            ],
        ),
    ]