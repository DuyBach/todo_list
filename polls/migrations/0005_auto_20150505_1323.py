# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20150504_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline_date',
            field=models.DateField(verbose_name='deadline'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='todo_text',
            field=models.CharField(max_length=160, verbose_name='todo'),
        ),
    ]
