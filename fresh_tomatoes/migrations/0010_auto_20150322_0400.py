# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fresh_tomatoes', '0009_auto_20150314_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='pilot',
            field=models.CharField(default='testing', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='show',
            name='pilot',
            field=models.CharField(default='testing', max_length=50),
            preserve_default=False,
        ),
    ]
