# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-29 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20190529_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image_loc',
            field=models.TextField(null=True),
        ),
    ]
