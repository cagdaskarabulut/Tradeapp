# Generated by Django 3.0.6 on 2022-02-14 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0048_auto_20220214_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradelog',
            name='indicatorResults',
            field=models.TextField(blank=True, default='', max_length=1000, null=True, verbose_name='İşlem sırasındaki indikatör değerleri'),
        ),
    ]
