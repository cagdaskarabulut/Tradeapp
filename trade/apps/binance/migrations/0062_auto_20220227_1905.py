# Generated by Django 3.0.6 on 2022-02-27 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0061_auto_20220227_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='targetPercentageForSellingForMargin',
            field=models.IntegerField(default=5, help_text='Margin Long veya Short için Satış yapılırken minimum yüzde x kadar kar edilmiş olması gerekir', verbose_name='Margin Long veya Short için Satış yapmak için beklenen min fark'),
        ),
    ]
