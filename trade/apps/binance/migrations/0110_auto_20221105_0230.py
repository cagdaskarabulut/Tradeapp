# Generated by Django 3.0.6 on 2022-11-04 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance', '0109_auto_20221105_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferences',
            name='cooldownAsHoursForNewBuyFromSameCoinBaseForRsi15Slow',
            field=models.IntegerField(default=12, help_text='Margin_RSI_15m ve RSI_15m Long için yeni alım yapmak için minimum (x * eldeki adet) kadar saat geçmeli', verbose_name='Margin_RSI_15m ve RSI_15m Long ve Short için taban cooldown saat sayisi'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='givenLimitHoursForRobot15mSlowThenTryToSell',
            field=models.FloatField(default=36, verbose_name='robot15mSlow Verilen saat kadar sat sinyali beklenecek, satılamazsa sürenin sonuna gelindiğinde trade 0.1 kar ve üzerindeyse hemen satılacak'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='isControlEmaForSellingPreviousRobot15mSlowTrades',
            field=models.BooleanField(default=True, verbose_name='EMA nın %5 altındaysa elinde RSI_15m_Slow robot ile alınmış coinler varsa sat'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='isRobot15mSlowActive',
            field=models.BooleanField(default=False, help_text='Ema üzerindeyken alım ve satım yapan, ema nın %5 altındayken stop olan RSI_15m_Slow robot çalışıyor mu?', verbose_name='RSI_15m_Slow robotu açık mı?'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='lastRobot15mSlowWorkingDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Son RSI_15m_Slow robotun çalışma tarihi'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='lossLimitForRobot15mSlow',
            field=models.FloatField(default=-100, help_text='Robotun bu zarar altına geldiğinde komple çalışmayacak. İstenirse sonradan arttırılabilir.', verbose_name='Robot RSI_15mSlow zarar limiti'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='maxLimitForRobot15mSlowAsUsdt',
            field=models.FloatField(default=400, help_text='RSI_15m_Slow Robotun kullanacağı maksimum usdt tutarı', verbose_name='Robot RSI_15m_Slow bütçe'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='maxOpenTradeCountForRobot15mSlow',
            field=models.IntegerField(default=2, help_text='RSI_15mSlow işlem için aynı coin adet limiti', verbose_name='RSI_15mSlow işlem için aynı coin adet limiti'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='maxRSIFor15mSlow',
            field=models.IntegerField(default=60, help_text='RSI_15m_Slow için Max RSI (Varsayılan değeri 65)', verbose_name='RSI_15m_Slow Max RSI'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='minRSIFor15mSlow',
            field=models.IntegerField(default=25, help_text='RSI_15m_Slow için Min RSI (Varsayılan değeri 20)', verbose_name='RSI_15m_Slow Min RSI'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='robot15mSlowNegativeSellCount',
            field=models.IntegerField(default=0, verbose_name='Robot RSI_15m_Slow zararına satış sayısı'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='robot15mSlowPositiveSellCount',
            field=models.IntegerField(default=0, verbose_name='Robot RSI_15m_Slow karlı satış sayısı'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='robot15mSlowResultHistoryAsUsdt',
            field=models.FloatField(default=0, help_text='Robot RSI_15mSlow geçmişten bu yana alım satımlardan yapılan kar zarar durumu', verbose_name='Robot RSI_15mSlow geçmişten bu yana alım satımlardan yapılan kar zarar durumu'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='robot15mSlowTotalBuyCount',
            field=models.IntegerField(default=0, verbose_name='Robot RSI_15m_Slow toplam alış sayısı'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='stopBuyingDateFor15mSlow',
            field=models.DateTimeField(blank=True, help_text='Robot15mSlow peş peşe 3 tane zararına satış yapıldığı zaman bu tarih alanını doldur ve 12 saat boyunca başka alım yapma. 12 saat sonra bu alanı boşaltıp tekrar alımlara devam et.', null=True, verbose_name='Robot15mSlow alış durduruşunun başlama tarihi (Değiştirilmez)'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='stopPercentageForSellingForRobot15mSlow',
            field=models.FloatField(default=-0.75, help_text='RSI_15m_Slow için zarar kes(stop) yapılacak yüzdelik oran', verbose_name='RSI_15m_Slow için zarar kes(stop) yapılacak yüzdelik oran'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='targetPercentageForSellingForRobot15mSlow',
            field=models.FloatField(default=0.75, help_text='RSI_15m_Slow için satış yapılırken minimum yüzde x kadar kar edilmiş olması gerekir', verbose_name='RSI_15m_Slow için Satış yapmak için beklenen min kar farkı'),
        ),
    ]
