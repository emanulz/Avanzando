# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_auto_20150425_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='adress',
            field=models.CharField(default=b'Sin direccion', max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
