# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0009_auto_20150430_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_code',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='credit_limit',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='identification',
            field=models.PositiveIntegerField(default=1, blank=True),
            preserve_default=False,
        ),
    ]
