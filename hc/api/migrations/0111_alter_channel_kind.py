# Generated by Django 5.1 on 2024-08-17 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0110_delete_hipchat_pagerteam_zendesk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='kind',
            field=models.CharField(choices=[('apprise', 'Apprise'), ('call', 'Phone Call'), ('discord', 'Discord'), ('email', 'Email'), ('gotify', 'Gotify'), ('group', 'Group'), ('linenotify', 'LINE Notify'), ('matrix', 'Matrix'), ('mattermost', 'Mattermost'), ('msteams', 'MS Teams Connector (stops working Oct 2024)'), ('msteamsw', 'Microsoft Teams'), ('ntfy', 'ntfy'), ('opsgenie', 'Opsgenie'), ('pagertree', 'PagerTree'), ('pd', 'PagerDuty'), ('po', 'Pushover'), ('pushbullet', 'Pushbullet'), ('rocketchat', 'Rocket.Chat'), ('shell', 'Shell Command'), ('signal', 'Signal'), ('slack', 'Slack'), ('sms', 'SMS'), ('spike', 'Spike'), ('telegram', 'Telegram'), ('trello', 'Trello'), ('victorops', 'Splunk On-Call'), ('webhook', 'Webhook'), ('whatsapp', 'WhatsApp'), ('zulip', 'Zulip')], max_length=20),
        ),
    ]