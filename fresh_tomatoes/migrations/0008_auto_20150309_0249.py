# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fresh_tomatoes', '0007_auto_20150309_0043'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoviePerson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=150)),
                ('movie', models.ForeignKey(to='fresh_tomatoes.Movie', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShowPerson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=150)),
                ('show', models.ForeignKey(to='fresh_tomatoes.Show', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='person',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='person',
            name='show',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
