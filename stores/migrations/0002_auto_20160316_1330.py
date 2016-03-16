# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stores',
            new_name='Store',
        ),
        migrations.AddField(
            model_name='item',
            name='expired',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='store',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='stores.Store'),
        ),
    ]
