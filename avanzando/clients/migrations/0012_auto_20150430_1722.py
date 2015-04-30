# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0011_client_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='credit',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='client',
            name='phone_number',
            field=models.PositiveIntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_code',
            field=models.PositiveIntegerField(),
        ),
    ]
