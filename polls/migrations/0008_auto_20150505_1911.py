# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20150505_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Deadline Date'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='todo_perc',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='percentage'),
        ),
    ]
