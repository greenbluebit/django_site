# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fresh_tomatoes', '0008_auto_20150309_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.CharField(max_length=55),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='show',
            name='rating',
            field=models.CharField(max_length=55),
            preserve_default=True,
        ),
    ]
