# Generated by Django 3.0.6 on 2022-02-28 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0065_totalbalancehistory_marginresulthistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='isControlEmaForMarginTrades',
            field=models.BooleanField(default=True, help_text='Margin tradelerde EMAyı kontrol ederek üstündeyken sadece Long , altındayken Long ve Short türlerinde alım yapar', verbose_name='Margin alımları için genel Ema kontrolü yap'),
        ),
    ]
