# Generated by Django 3.0.6 on 2022-01-22 15:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0030_auto_20220122_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='preferredCompareCoinName',
            field=models.TextField(default='BTC', help_text='Karşılaştırılacak coin adı borsada karşılığı olduğu sürece btc girilmesi tavsiye edilir.', max_length=100, verbose_name='Karşılaştırılacak coin adı'),
        ),
        migrations.AlterField(
            model_name='processlog',
            name='processDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, help_text='Islem Tarihi', verbose_name='Islem Tarihi'),
        ),
        migrations.AlterField(
            model_name='totalbalancehistory',
            name='freeUsdt',
            field=models.FloatField(default=0, help_text='Boşta bekleten Usdt (Spot taki Free duran usdt miktarından bulunur. Robotun mevcut toplam parası hesaplanırken burası ile robotun kullanıdığı toplanır. ', verbose_name='Bekleyen Usdt'),
        ),
        migrations.AlterField(
            model_name='totalbalancehistory',
            name='manuelUsing',
            field=models.FloatField(default=0, help_text='Manuel alım yapılarak kullanımda olanların toplam Usdt değeri', verbose_name='Manuel kullanılan Usdt'),
        ),
        migrations.AlterField(
            model_name='totalbalancehistory',
            name='robotUsing',
            field=models.FloatField(default=0, help_text='Robotun aktif olarak kullandığı toplam tutar', verbose_name='Robot kullanıyor'),
        ),
        migrations.AlterField(
            model_name='totalbalancehistory',
            name='transactionDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, help_text='İşlemin kayıt tarihi', verbose_name='İşlem tarihi'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='buyedByRobot',
            field=models.BooleanField(default=True, help_text='Robot tarafından mı alındı?', verbose_name='Robot mu aldı?'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='coin',
            field=models.ForeignKey(help_text='Coin adı burada girilir.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='trade_coin', to='binance.Coin', verbose_name='Coin adı'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='count',
            field=models.FloatField(default=0, help_text='Elde kalan mevcut adet . Satışlardan sonra güncellenir.', verbose_name='Elde kalan mevcut adet'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='differentExchangeName',
            field=models.TextField(default='Binance', help_text='Varsayılan olarak Binance girilir fakat farklı borsada ise o borsanın adı girilir', max_length=1000, null=True, verbose_name='Farklı Borsanın Adı'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='exchangePair',
            field=models.ForeignKey(help_text='Fiyat çifti tercihen Usdt girilir.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='trade_exchangePair', to='binance.Coin', verbose_name='Fiyat çifti'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='firstCount',
            field=models.FloatField(default=0, help_text='Ilk alınan adet (Satışlardan önce). Satışlardan sonra güncellenmez.', verbose_name='Ilk alınan adet'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='firstPriceAgainstBtc',
            field=models.FloatField(default=0, help_text='Alış fiyat Btc karşılığı olarak', verbose_name='Alış fiyatı Btc'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='howManyTimesSold',
            field=models.IntegerField(default=0, help_text='Kaç defa satıldı?', verbose_name='Satılma sayısı'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='indicatorResults',
            field=models.TextField(blank=True, default='', help_text='Son çalıştığında alınan indicatorlerin güncel durumları tutulur.(Alım modu açık ise her çalışmada güncellenir.)', max_length=1000, null=True, verbose_name='Son çalıştığındaki indicatorlerin durumları'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='isDifferentExchange',
            field=models.BooleanField(default=False, help_text='Farklı Borsada Mı (Borsada bulunan tutar USDT olarak girilir)?', verbose_name='Farklı Borsada Mı?'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='isPassiveInEarn',
            field=models.BooleanField(default=False, help_text='Kazan bölümünde mi ? (Eğer öyle ise satış yapılmaz sadece görüntülenir.)', verbose_name='Kazan bölümünde mi?'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='lastSellDate',
            field=models.DateField(blank=True, help_text='Satış yapıldığında tarih girilir', null=True, verbose_name='Son satış tarihi'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='price',
            field=models.FloatField(default=0, help_text='Alış fiyatı Usdt olarak', verbose_name='Alış fiyatı Usdt'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='temp_currentPrice',
            field=models.FloatField(default=0, help_text='Şimdiki Fiyatı Usdt - Veritabanına yazılmaz anlık olarak çekilir', verbose_name='Şimdiki Fiyatı Usdt'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='temp_differenceToBTCPercentage',
            field=models.FloatField(default=0, help_text='Mevcut yüzdelik kar/zarar BTC - Veritabanına yazılmaz anlık olarak çekilir', verbose_name='Mevcut yüzdelik kar/zarar BTC'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='temp_differenceTotalAsUSDT',
            field=models.FloatField(default=0, help_text='Kar/Zarar farkının usdt olarak tutulduğu alan - Veritabanına yazılmaz anlık olarak çekilir', verbose_name='Kar/Zarar farkı USDT'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='temp_profitLossPercentage',
            field=models.FloatField(default=0, help_text='Mevcut yüzdelik kar/zarar USDT - Veritabanına yazılmaz anlık olarak çekilir', verbose_name='Mevcut yüzdelik kar/zarar USDT'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='temp_profitLossTimes',
            field=models.FloatField(default=0, help_text='Mevcut kaç katı kar/zarar - Veritabanına yazılmaz anlık olarak çekilir', verbose_name='Mevcut kaç katı kar/zarar'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='temp_ratioToTotalPercentage',
            field=models.FloatField(default=0, help_text='Toplam mal varlığındaki kapladığı yüzdelik yer - Veritabanına yazılmaz anlık olarak çekilir', verbose_name='Toplam mal varlığına oranı'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='temp_totalCurrentPrice',
            field=models.FloatField(default=0, help_text='Mevcut toplam fiyatı - Veritabanına yazılmaz, gerektiğinde anlık olarak getActivePrice*count şeklinde kullanılır ', verbose_name='Mevcut toplam fiyatı'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='transactionDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, help_text='Alımın yapıldığı tarih otomatik olarak alım yapıldığında girilir', verbose_name='Alış Tarihi'),
        ),
    ]
