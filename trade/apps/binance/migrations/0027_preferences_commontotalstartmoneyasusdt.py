# Generated by Django 3.0.6 on 2022-01-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0026_auto_20220118_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferences',
            name='commonTotalStartMoneyAsUSDT',
            field=models.FloatField(default=0),
        ),
    ]
