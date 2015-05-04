# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='todo_perc',
            field=models.IntegerField(max_length=100, verbose_name='perc', default=0),
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline_date',
            field=models.DateTimeField(verbose_name='deadline'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='todo_text',
            field=models.CharField(max_length=200, verbose_name='todo'),
        ),
    ]
