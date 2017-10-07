# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_auto_20141105_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='keys',
            name='twitter_token',
            field=models.CharField(blank=True, max_length=50, null=True),
            preserve_default=True,
        ),
    ]
