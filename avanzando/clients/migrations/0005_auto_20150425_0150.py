# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20150425_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='credit_limit',
            field=models.FloatField(default=b'0', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='identification',
            field=models.IntegerField(default=b'0', null=True, blank=True),
        ),
    ]
