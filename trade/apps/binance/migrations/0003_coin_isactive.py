# Generated by Django 3.0.6 on 2021-12-26 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0002_coin_trade'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='isActive',
            field=models.BooleanField(default=True, help_text='Aktif mi ?', verbose_name='Aktif mi ?'),
        ),
    ]
