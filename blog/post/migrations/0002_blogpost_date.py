# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 3, 3, 22, 13, 50, 768200, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
