# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-27 16:28
from __future__ import unicode_literals

from django.db import migrations


def convert_to_json(apps, schema_editor):
    EmailMessage = apps.get_model('postmark.EmailMessage')
    for e in EmailMessage.objects.all():
        e.attachments = e.attachments.replace('\'', '"').replace(': u"', ': "')
        if e.attachments == '':
            e.attachments = '[]'
        e.save(update_fields=['attachments'])


class Migration(migrations.Migration):

    dependencies = [
        ('postmark', '0007_auto_20161219_1100'),
    ]

    operations = [
        migrations.RunPython(convert_to_json, migrations.RunPython.noop)
    ]
