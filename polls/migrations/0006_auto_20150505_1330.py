# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20150505_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline_date',
            field=models.DateField(),
        ),
    ]
