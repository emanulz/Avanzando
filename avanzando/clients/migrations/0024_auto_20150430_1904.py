# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0023_auto_20150430_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='credit',
            field=models.BooleanField(default=0, verbose_name=b'Tiene cr\xc3\xa9dito'),
        ),
    ]
