# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20150430_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='inventory_amount',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='inventory_minimum',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
