# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0013_auto_20150430_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='adress',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='credit_limit',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='identification',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.PositiveIntegerField(default=0, null=True, blank=True),
        ),
    ]
