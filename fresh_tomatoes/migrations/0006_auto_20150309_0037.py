# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fresh_tomatoes', '0005_movie_budget'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='project',
            name='person',
        ),
        migrations.RemoveField(
            model_name='project',
            name='show',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.AddField(
            model_name='movie',
            name='contribuitor',
            field=models.ForeignKey(to='fresh_tomatoes.Person', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='show',
            name='contribuitor',
            field=models.ForeignKey(to='fresh_tomatoes.Person', null=True),
            preserve_default=True,
        ),
    ]
