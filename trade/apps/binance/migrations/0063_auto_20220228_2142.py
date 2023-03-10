# Generated by Django 3.0.6 on 2022-02-28 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0062_auto_20220227_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preferences',
            name='marginResultHistoryAsUsdt',
        ),
        migrations.RemoveField(
            model_name='preferences',
            name='usedLimitForMarginAsUsdt',
        ),
        migrations.AlterField(
            model_name='preferences',
            name='cooldownAsHoursForNewBuyFromSameCoinBaseForMargin',
            field=models.IntegerField(default=12, help_text='Yeni alım yapmak için minimum (x * eldeki adet) kadar saat geçmeli', verbose_name='Margin Long ve Short için taban cooldown saat sayisi'),
        ),
    ]
