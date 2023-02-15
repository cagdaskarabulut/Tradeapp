# Generated by Django 3.0.6 on 2022-01-22 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0032_auto_20220122_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalbalancehistory',
            name='totalCommonTl',
            field=models.FloatField(default=0, help_text='Genel Durum TL - Oto. Anlık Toplam TL:', verbose_name='Genel Durum TL - Oto. Anlık Toplam TL:'),
        ),
        migrations.AddField(
            model_name='totalbalancehistory',
            name='totalCommonUsdt',
            field=models.FloatField(default=0, help_text='Genel Durum USDT - Oto. Anlık Toplam', verbose_name='Genel Durum USDT - Oto. Anlık Toplam'),
        ),
        migrations.AddField(
            model_name='totalbalancehistory',
            name='totalEarn',
            field=models.FloatField(default=0, help_text='Kazan -Yeni toplam', verbose_name='Kazan -Yeni toplam'),
        ),
        migrations.AddField(
            model_name='totalbalancehistory',
            name='totalOtherExchanges',
            field=models.FloatField(default=0, help_text='Diğer - Diğer Borsalar Son Hali', verbose_name='Diğer - Diğer Borsalar Son Hali'),
        ),
        migrations.AddField(
            model_name='totalbalancehistory',
            name='totalRobot',
            field=models.FloatField(default=0, help_text='Robot Son durum', verbose_name='Robot Son durum'),
        ),
        migrations.AlterField(
            model_name='totalbalancehistory',
            name='manuelUsing',
            field=models.FloatField(default=0, help_text='Manuel Alınanlar Son Halinin toplam Usdt değeri', verbose_name='Manuel Alınanlar Son Hali'),
        ),
    ]
