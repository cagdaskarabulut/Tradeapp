# Generated by Django 3.0.6 on 2022-09-12 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0097_preferences_temp_draftusdtdiffdateaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradelog',
            name='passedHoursToSell',
            field=models.IntegerField(default=0, verbose_name='Kaç saatte satıldı?'),
        ),
    ]
