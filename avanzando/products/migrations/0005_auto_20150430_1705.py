# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_categories', '0002_auto_20150430_1604'),
        ('products', '0004_auto_20150430_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, to='product_categories.Product_Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='inventory_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='inventory_minimum',
            field=models.IntegerField(default=0),
        ),
    ]
