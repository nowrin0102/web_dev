# Generated by Django 3.1.4 on 2021-01-10 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_remove_poll_option_four_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='option_four_count',
            field=models.IntegerField(default=0),
        ),
    ]
