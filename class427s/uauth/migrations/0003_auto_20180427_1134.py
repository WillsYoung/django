# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-27 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uauth', '0002_users_u_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='u_password',
            field=models.CharField(max_length=100),
        ),
    ]