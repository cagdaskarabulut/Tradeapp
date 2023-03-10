# Generated by Django 3.0.6 on 2022-03-20 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0077_totalbalancehistory_robot15mresulthistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='isUsableForRSI15m',
            field=models.BooleanField(default=False, verbose_name='RSI15 için uygun coin mi?'),
        ),
        migrations.AlterField(
            model_name='coin',
            name='isMargin',
            field=models.BooleanField(default=False, verbose_name='Kardıraçlı coin mi?'),
        ),
    ]
