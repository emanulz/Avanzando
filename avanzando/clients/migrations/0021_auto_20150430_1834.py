# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0020_auto_20150430_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='identification',
            field=models.CharField(max_length=255, null=True, verbose_name='C\xe9dula', blank=True),
        ),
    ]
