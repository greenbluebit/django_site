# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fresh_tomatoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='budget',
            field=models.CharField(default=b'1', max_length=150),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='goofs',
            field=models.TextField(default=b' '),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='trivia',
            field=models.TextField(default=b' '),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='show',
            name='seasons',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
