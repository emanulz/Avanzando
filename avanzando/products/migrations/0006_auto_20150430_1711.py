# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20150430_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='email',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, to='product_categories.Product_Category'),
        ),
    ]
