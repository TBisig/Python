# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-29 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaction',
            name='plannedby',
        ),
        migrations.AddField(
            model_name='vaction',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Vacations', to='User.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vaction',
            name='enddate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='vaction',
            name='startdate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='vaction',
            name='users',
            field=models.ManyToManyField(to='User.User'),
        ),
    ]
