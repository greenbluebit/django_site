# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fresh_tomatoes', '0003_auto_20150306_0425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='budgets',
        ),
    ]
