# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0016_auto_20150430_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='afiliate_code',
            field=models.PositiveIntegerField(default=b'0', blank=True),
        ),
    ]
