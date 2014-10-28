# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postmark', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailbounce',
            name='can_activate',
            field=models.BooleanField(default=False, verbose_name='Can Activate'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emailbounce',
            name='inactive',
            field=models.BooleanField(default=False, verbose_name='Inactive'),
            preserve_default=True,
        ),
    ]
