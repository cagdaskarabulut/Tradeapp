# Generated by Django 3.0.6 on 2021-12-26 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0003_coin_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='coin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='trade_coin', to='binance.Coin'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='exchangePair',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='trade_exchangePair', to='binance.Coin'),
        ),
    ]
