# Generated by Django 3.0.6 on 2022-03-09 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0068_totalbalancehistory_robotresulthistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferences',
            name='marginRobotNegativeSellCount',
            field=models.IntegerField(default=-30, verbose_name='Margin robot zararına satış sayısı'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='marginRobotPositiveSellCount',
            field=models.IntegerField(default=-30, verbose_name='Margin robot karlı satış sayısı'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='marginRobotTotalBuyCount',
            field=models.IntegerField(default=-30, verbose_name='Margin robot toplam alış sayısı'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='robotNegativeSellCount',
            field=models.IntegerField(default=-30, verbose_name='Robot zararına satış sayısı'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='robotPositiveSellCount',
            field=models.IntegerField(default=-30, verbose_name='Robot karlı satış sayısı'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='robotTotalBuyCount',
            field=models.IntegerField(default=-30, verbose_name='Robot toplam alış sayısı'),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='isControlEmaForSellingPreviousMarginTrades',
            field=models.BooleanField(default=False, help_text='EMA üzerindeyse elinde BTCDOWN varsa sat', verbose_name='EMA üzerindeyse elinde BTCDOWN varsa sat'),
        ),
    ]
