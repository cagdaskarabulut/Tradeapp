# Generated by Django 3.0.6 on 2022-01-17 17:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0020_trade_temp_totalcurrentprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processResult', models.TextField(help_text='Islem Durumu', max_length=100, null=True, verbose_name='Islem Durumu')),
                ('processDate', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('processSubject', models.TextField(help_text='Islem Basligi', max_length=100, null=True, verbose_name='Islem Basligi')),
                ('processDetails', models.TextField(help_text='Islem Detayi', max_length=100000, null=True, verbose_name='Islem Detayi')),
            ],
        ),
    ]