# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0, null=True, blank=True)),
                ('fractioned', models.BooleanField(default=False)),
                ('taxes', models.BooleanField(default=True)),
                ('taxes_amount', models.FloatField(default=0, blank=True)),
            ],
        ),
    ]
