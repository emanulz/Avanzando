# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20150425_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='adress',
            field=models.CharField(default=b'Sin direccion', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_code',
            field=models.IntegerField(default=b'0', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='identification',
            field=models.IntegerField(default=b'0', blank=True),
        ),
    ]
