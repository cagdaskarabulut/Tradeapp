# Generated by Django 3.0.6 on 2022-11-02 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0105_auto_20221101_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferences',
            name='waitHoursAfterNegativeSell',
            field=models.FloatField(default=3.0, verbose_name='Negatif satıştan sonra yeni alış yapabilmek için beklemesi gereken saat sayısı'),
        ),
    ]
