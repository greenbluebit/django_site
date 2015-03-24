# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_text', models.CharField(max_length=250)),
                ('plot', models.TextField()),
                ('rating', models.CharField(max_length=5)),
                ('poster', models.TextField()),
                ('available_imax', models.BooleanField(default=False)),
                ('available_3d', models.BooleanField(default=False)),
                ('release_date', models.DateField()),
                ('duration', models.CharField(max_length=100)),
                ('trailer_youtube_url', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie', models.ForeignKey(to='fresh_tomatoes.Movie')),
                ('person', models.ForeignKey(to='fresh_tomatoes.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_text', models.CharField(max_length=250)),
                ('plot', models.TextField()),
                ('rating', models.CharField(max_length=5)),
                ('poster', models.TextField()),
                ('available_imax', models.BooleanField(default=False)),
                ('available_3d', models.BooleanField(default=False)),
                ('release_date', models.DateField()),
                ('seasons', models.IntegerField()),
                ('network', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='show',
            field=models.ForeignKey(to='fresh_tomatoes.Show'),
            preserve_default=True,
        ),
    ]
