# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import clients.models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0022_auto_20150430_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='adress',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Direcci\xc3\xb3n', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='afiliate_code',
            field=models.PositiveIntegerField(default=0, verbose_name=b'N\xc3\xbamero de asociado', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='credit',
            field=models.BooleanField(default=0, verbose_name=b'Cr\xc3\xa9dito'),
        ),
        migrations.AlterField(
            model_name='client',
            name='credit_limit',
            field=models.FloatField(default=0, verbose_name=b'L\xc3\xadmite de cr\xc3\xa9dito', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(default=clients.models.phone_default, max_length=9, null=True, verbose_name=b'N\xc3\xbamero de tel\xc3\xa9fono', blank=True),
        ),
    ]
