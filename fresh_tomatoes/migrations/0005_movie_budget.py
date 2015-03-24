# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fresh_tomatoes', '0004_remove_movie_budgets'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='budget',
            field=models.TextField(default=b' '),
            preserve_default=True,
        ),
    ]
