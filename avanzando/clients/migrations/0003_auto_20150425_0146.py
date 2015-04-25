# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20150425_0145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='clientCode',
            new_name='client_code',
        ),
    ]
