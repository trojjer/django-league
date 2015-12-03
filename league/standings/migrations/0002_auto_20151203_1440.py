# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-03 14:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('standings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teamstanding',
            options={'get_latest_by': 'source_timestamp'},
        ),
        migrations.AddField(
            model_name='teamstanding',
            name='competition',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teamstanding',
            name='season',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teamstanding',
            name='source_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 3, 14, 40, 24, 951738, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teamstanding',
            name='team_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='teamstanding',
            unique_together=set([('source_timestamp', 'team_id', 'competition', 'season')]),
        ),
    ]
