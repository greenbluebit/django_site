# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fresh_tomatoes', '0006_auto_20150309_0037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='contribuitor',
        ),
        migrations.RemoveField(
            model_name='show',
            name='contribuitor',
        ),
        migrations.AddField(
            model_name='person',
            name='movie',
            field=models.ForeignKey(to='fresh_tomatoes.Movie', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='show',
            field=models.ForeignKey(to='fresh_tomatoes.Show', null=True),
            preserve_default=True,
        ),
    ]
