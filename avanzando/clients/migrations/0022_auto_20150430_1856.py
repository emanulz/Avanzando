# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0021_auto_20150430_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='identification',
            field=models.CharField(max_length=255, null=True, verbose_name=b'C\xc3\xa9dula', blank=True),
        ),
    ]
