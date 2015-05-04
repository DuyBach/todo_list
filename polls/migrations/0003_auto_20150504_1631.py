# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150504_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_perc',
            field=models.IntegerField(default=0, verbose_name='perc'),
        ),
    ]
