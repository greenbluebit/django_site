# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fresh_tomatoes', '0002_auto_20150306_0407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='budget',
        ),
        migrations.AddField(
            model_name='movie',
            name='budgets',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
