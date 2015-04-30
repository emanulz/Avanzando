# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0014_auto_20150430_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_code',
            field=models.PositiveIntegerField(),
        ),
    ]
