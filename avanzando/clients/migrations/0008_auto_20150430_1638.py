# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_auto_20150425_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_code',
            field=models.PositiveIntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='credit_limit',
            field=models.FloatField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='identification',
            field=models.PositiveIntegerField(default=0, null=True, blank=True),
        ),
    ]
