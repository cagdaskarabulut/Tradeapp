# Generated by Django 3.0.6 on 2022-01-27 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0038_totalbalancehistory_btc'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferences',
            name='lastRobotWorkingDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Son robotub çalışma tarihi'),
        ),
    ]
