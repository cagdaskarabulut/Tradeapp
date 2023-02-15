# Generated by Django 3.0.6 on 2022-03-09 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0069_auto_20220309_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='marginRobotNegativeSellCount',
            field=models.IntegerField(default=0, verbose_name='Margin robot zararına satış sayısı'),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='marginRobotPositiveSellCount',
            field=models.IntegerField(default=0, verbose_name='Margin robot karlı satış sayısı'),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='marginRobotTotalBuyCount',
            field=models.IntegerField(default=0, verbose_name='Margin robot toplam alış sayısı'),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='robotNegativeSellCount',
            field=models.IntegerField(default=0, verbose_name='Robot zararına satış sayısı'),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='robotPositiveSellCount',
            field=models.IntegerField(default=0, verbose_name='Robot karlı satış sayısı'),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='robotTotalBuyCount',
            field=models.IntegerField(default=0, verbose_name='Robot toplam alış sayısı'),
        ),
    ]