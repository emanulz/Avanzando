# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_auto_20150430_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='adress',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_code',
            field=models.PositiveIntegerField(default=1, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='credit_limit',
            field=models.FloatField(default=1, blank=True),
        ),
    ]
