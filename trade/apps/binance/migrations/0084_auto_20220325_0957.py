# Generated by Django 3.0.6 on 2022-03-25 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0083_auto_20220325_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradelog',
            name='gainUsdt',
            field=models.FloatField(default=0, verbose_name='Kar/Zarar USDT olarak'),
        ),
        migrations.AlterField(
            model_name='tradelog',
            name='profitLossPercentage',
            field=models.FloatField(default=0, help_text='İşlem sonucunda yapılmış olan yüzdelik kar/zarar USDT', verbose_name='Kar/zarar USDT üzerinden Yüzdelik olarak'),
        ),
    ]
