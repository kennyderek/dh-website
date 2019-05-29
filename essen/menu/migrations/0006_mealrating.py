# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-28 21:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_autolateplate'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('rating', models.IntegerField(null=True)),
                ('comment', models.TextField(null=True)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Meal')),
            ],
        ),
    ]