# Generated by Django 3.0.6 on 2022-02-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0053_auto_20220224_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preferences',
            name='stopPercentageForSellingForLong',
        ),
        migrations.RemoveField(
            model_name='preferences',
            name='targetPercentageForSellingForLong',
        ),
        migrations.AddField(
            model_name='preferences',
            name='marginResultHistoryAsUsdt',
            field=models.FloatField(default=0, help_text='Margin geçmişten bu yana alım satımlardan yapılan kar zarar durumu', verbose_name='Margin geçmişten bu yana alım satımlardan yapılan kar zarar durumu'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='stopPercentageForSellingForMargin',
            field=models.IntegerField(default=-30, help_text='Margin Long için zarar kes yapılacak yüzdelik oran', verbose_name='Margin Long için zarar kes yapılacak yüzdelik oran'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='targetPercentageForSellingForMargin',
            field=models.IntegerField(default=5, help_text='Margin Long için Satış yapılırken minimum yüzde x kadar kar edilmiş olması gerekir', verbose_name='Margin Long için Satış yapmak için beklenen min fark'),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='maxLimitForMarginAsUsdt',
            field=models.FloatField(default=50, help_text='Margin Long robotun kullanacağı maksimum usdt tutarı', verbose_name='Margin Bütçe'),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='usedLimitForMarginAsUsdt',
            field=models.FloatField(default=0, help_text='Margin Long robotun kullandığı toplam usdt tutarı', verbose_name='Margin Bütçeden Kullanılan'),
        ),
    ]