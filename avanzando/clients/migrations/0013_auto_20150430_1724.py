# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0012_auto_20150430_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_code',
            field=models.PositiveIntegerField(max_length=6),
        ),
    ]
