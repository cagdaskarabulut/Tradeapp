# Generated by Django 3.0.6 on 2022-02-09 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0043_auto_20220207_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradelog',
            name='profitLossPercentage',
            field=models.FloatField(default=0, help_text='İşlem sonucunda yapılmış olan yüzdelik kar/zarar USDT', verbose_name='Yüzdelik kar/zarar USDT'),
        ),
    ]
