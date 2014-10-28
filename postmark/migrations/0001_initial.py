# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailBounce',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('inactive', models.BooleanField(verbose_name='Inactive')),
                ('can_activate', models.BooleanField(verbose_name='Can Activate')),
                ('type', models.CharField(max_length=100, verbose_name='Type', choices=[(b'HardBounce', 'Hard Bounce'), (b'Transient', 'Transient'), (b'Unsubscribe', 'Unsubscribe'), (b'Subscribe', 'Subscribe'), (b'AutoResponder', 'Auto Responder'), (b'AddressChange', 'Address Change'), (b'DnsError', 'DNS Error'), (b'SpamNotification', 'Spam Notification'), (b'OpenRelayTest', 'Open Relay Test'), (b'Unknown', 'Unknown'), (b'SoftBounce', 'Soft Bounce'), (b'VirusNotification', 'Virus Notification'), (b'ChallengeVerification', 'Challenge Verification'), (b'BadEmailAddress', 'Bad Email Address'), (b'SpamComplaint', 'Spam Complaint'), (b'ManuallyDeactivated', 'Manually Deactivated'), (b'Unconfirmed', 'Unconfirmed'), (b'Blocked', 'Blocked')])),
                ('description', models.TextField(verbose_name='Description')),
                ('details', models.TextField(verbose_name='Details')),
                ('bounced_at', models.DateTimeField(verbose_name='Bounced At')),
            ],
            options={
                'ordering': ['-bounced_at'],
                'get_latest_by': 'bounced_at',
                'verbose_name': 'email bounce',
                'verbose_name_plural': 'email bounces',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmailMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_id', models.CharField(max_length=40, verbose_name='Message ID')),
                ('submitted_at', models.DateTimeField(verbose_name='Submitted At')),
                ('status', models.CharField(max_length=150, verbose_name='Status')),
                ('to', models.CharField(max_length=150, verbose_name='To')),
                ('to_type', models.CharField(max_length=3, verbose_name='Type', choices=[(b'to', 'Recipient'), (b'cc', 'Carbon Copy'), (b'bcc', 'Blind Carbon Copy')])),
                ('sender', models.CharField(max_length=150, verbose_name='Sender')),
                ('reply_to', models.CharField(max_length=150, verbose_name='Reply To')),
                ('subject', models.CharField(max_length=150, verbose_name='Subject')),
                ('tag', models.CharField(max_length=150, verbose_name='Tag')),
                ('text_body', models.TextField(verbose_name='Text Body')),
                ('html_body', models.TextField(verbose_name='HTML Body')),
                ('headers', models.TextField(verbose_name='Headers')),
                ('attachments', models.TextField(verbose_name='Attachments')),
            ],
            options={
                'ordering': ['-submitted_at'],
                'get_latest_by': 'submitted_at',
                'verbose_name': 'email message',
                'verbose_name_plural': 'email messages',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='emailbounce',
            name='message',
            field=models.ForeignKey(related_name='bounces', verbose_name='Message', to='postmark.EmailMessage'),
            preserve_default=True,
        ),
        migrations.AlterOrderWithRespectTo(
            name='emailbounce',
            order_with_respect_to='message',
        ),
    ]
