# Generated by Django 3.0.6 on 2022-02-01 20:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0041_remove_tradelog_buyedbyrobot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradelog',
            name='count',
            field=models.FloatField(default=0, verbose_name='Adet'),
        ),
        migrations.AlterField(
            model_name='tradelog',
            name='price',
            field=models.FloatField(default=0, help_text='Fiyat Usdt olarak', verbose_name='Fiyat Usdt'),
        ),
        migrations.AlterField(
            model_name='tradelog',
            name='transactionDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='İşlem Tarihi'),
        ),
    ]
