# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-22 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20160722_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.DecimalField(decimal_places=1, max_digits=8),
        ),
    ]
