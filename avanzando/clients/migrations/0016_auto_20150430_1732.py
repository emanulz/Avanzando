# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0015_auto_20150430_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='client_code',
        ),
        migrations.AddField(
            model_name='client',
            name='afiliate_code',
            field=models.PositiveIntegerField(default=0, blank=True),
        ),
    ]
