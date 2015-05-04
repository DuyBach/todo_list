# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20150504_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_perc',
            field=models.IntegerField(verbose_name='perc', default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
