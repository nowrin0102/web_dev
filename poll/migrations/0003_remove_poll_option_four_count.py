# Generated by Django 3.1.4 on 2021-01-10 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_poll_option_four_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='option_four_count',
        ),
    ]
