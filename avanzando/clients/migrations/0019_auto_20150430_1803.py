# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import clients.models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0018_auto_20150430_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='afiliate_code',
            field=models.PositiveIntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='credit_limit',
            field=models.FloatField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(default=clients.models.phone_default, max_length=9, null=True, blank=True),
        ),
    ]
