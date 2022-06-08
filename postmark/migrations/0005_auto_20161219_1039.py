# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-19 10:39
from __future__ import unicode_literals

import json

from django.db import migrations
from django.utils.encoding import force_str


def set_hstore(apps, schema_editor):
    EmailMessage = apps.get_model('postmark.EmailMessage')

    def transform(d):
        return {
            item['Name']: force_str(item['Value'])
            for item in d
        }

    for e in EmailMessage.objects.all():
        if e.headers == '':
            e.headers_hstore = {}
        else:
            e.headers_hstore = transform(json.loads(e.headers.replace('\'', '"')))
        e.save(update_fields=['headers_hstore'])


class Migration(migrations.Migration):

    dependencies = [
        ('postmark', '0004_emailmessage_headers_hstore'),
    ]

    operations = [
        migrations.RunPython(set_hstore)
    ]
