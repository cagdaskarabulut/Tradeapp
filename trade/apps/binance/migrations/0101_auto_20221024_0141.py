# Generated by Django 3.0.6 on 2022-10-23 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0100_totalbalancehistory_marginbtcresulthistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferences',
            name='givenLimitHoursForRobot15mThenTryToSell',
            field=models.IntegerField(default=4, verbose_name='Verilen saat kadar sat sinyali beklenecek, satılamazsa sürenin sonuna gelindiğinde trade 0.1 kar ve üzerindeyse hemen satılacak'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='givenLimitHoursForRobotMarginThenTryToSell',
            field=models.IntegerField(default=2, verbose_name='Verilen saat kadar sat sinyali beklenecek, satılamazsa sürenin sonuna gelindiğinde trade 0.1 kar ve üzerindeyse hemen satılacak'),
        ),
    ]
