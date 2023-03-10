# Generated by Django 3.0.6 on 2022-01-23 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0033_auto_20220123_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='isBuyAutomaticallyAfterPanicMode',
            field=models.BooleanField(default=False, help_text='Panik modundan otomatik çıkış açıkken panik modundan çıkış aşamasında bu alanı kontrol eder ve işaretli ise otomatik olarak birer kademe alır.', verbose_name='Panik modundan çıkışta otomatik al'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='isBuyAutomaticallyAfterPanicMode',
            field=models.BooleanField(default=True, help_text='Panik modundan otomatik çıkış açıkken panik modundan çıkış aşamasında bu alanı kontrol eder ve işaretli ise otomatik olarak birer kademe alır.', verbose_name='Panik modundan çıkışta otomatik coin al'),
        ),
    ]
