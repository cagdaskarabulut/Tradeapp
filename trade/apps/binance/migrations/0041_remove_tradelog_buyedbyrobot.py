# Generated by Django 3.0.6 on 2022-02-01 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0040_tradelog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tradelog',
            name='buyedByRobot',
        ),
    ]
