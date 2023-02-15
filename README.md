#TRADEAPP
Python, django teknolojileri ile geliştirilmiş celery ile periodik olarak otomatik çalışarak belirli algoritmalara göre alım/satım yaparn Binance ile entegre çalışan trade uygulamasıdır.

##Çalıştırmak için 4 farlı terminal sayfasında venv aktive edip aşağıdaki komutlar herbir terminal ekranında çalıştırılır
1- python manage.py runserver 127.0.0.1:8000
2- redis-server
3- celery -A trade worker -l INFO
4- celery -A trade beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

##Kurulum
1-) pip kurulum => mac => 1-) curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py 2-) python3 get-pip.py
2-) Python kurulur => "https://www.python.org/downloads/" adresinden
3-) virtualenv => windows: pip install virtualenv , mac : sudo pip install virtualenv
4-) virtualenv projeye eklemek için proje klasörünün paraleline=>  windows:"python3 -m venv venv_projeadı", 
mac Yeni : virtualenv venv_projeadı -p python3 , mac Eskisi : virtualenv venv_projeadı -p python

5-) Kurmuş olduğumuz virtualenv i aktif hale getirmek için=> windows:venv\Scripts\ altındaki activate çalıştırılır,  
mac: "source venv/bin/activate" çalıştırılır.

6-) Varolan bir proje tanıtılıyorsa eski kütüphanelerini indirmek için => pip install -r requirements.txt
7) Yok ise Django kurulum => "pip install django", Son sürüm Django update => "pip install django --upgrade"

8-) Yeni proje yaratmak için => django-admin startproject myproject

9-) Proje altında 'blog' isminde yeni bir modül oluşturmak istediğim zaman => python manage.py startapp binance

daha sonra yaratilan binance projesinin klasoru ornek resimdeki gibi ana proje klasoru altinda apps adinda bir klasor olusturulup onun altina tasinir

10-) Modeli veritabanına migrate etmek => 
    a) başlama => "python manage.py makemigrations" veya "python manage.py makemigrations projeAdı"
    b) tamamlama => "python manage.py migrate" veya "python manage.py migrate projeAdı"

11-) Veritabanında oluşturulmamış tablolar varsa şu komutu çalıştır => python manage.py migrate --run-syncdb
bu da olmazda proje altındaki db.sqllite3 ü silip migrate deneyelim

12-) Kullanıcı yaratmak (admin panel için superuser) => python manage.py createsuperuser

13-) shell de kod çalıştırabilek için kurulum => pip install django-extensions 

14-) shell i başlatmak için komut (sql ile anlık kod yazabilmek için)=> python manage.py shell veya python manage.py shell_plus 

15-) static dosyalar için "settings.py" dosyası altında değişiklikler yapılıyor. 
Eklenen başlıklar : STATIC_URL , STATICFILES_DIRS, STATIC_ROOT 
 STATIC_ROOT altında tüm static dosyaları birleştirmek için çalıştırılacak komut :  *** python manage.py collectstatic
temizlemek için : python manage.py collectstatic --noinput --clear

16-) "pip freeze > requirements.txt" => Projeyi farklı ortamlara kurmak için  ile requirements dosyası olusturulur. 
"pip install -r requirements.txt" => Kurulum yapılacak yerde tamamını yüklemek için  komutu çalıştıırlır. Belli şeyleri yüklemek için ise pip show <packagename>
Pipdeptree
pip-compile and pip-sync
pip-compile --upgrade => sonradan farklılıkları almak için

17-) mevcut yüklü libleri görmek için => pip freeze

18-) modeldeki nesneleri veribanaı işlemlerini yapmak için venv e bağlanıp "pip install django-extensions " kurulur ve kullanmak için terminalde "python manage.py shell_plus " komutu ile çalıştırılır. Kullanım örneği : "EtabsCorrMatch.objects.count()"


EK BILGILER
______________

TradeBot uygulaması için TA-Lib kurulması gerekiyor. Windows ve mac için gerekli dosyalar git lib klasörü içerisinde var. Windows için dosya direk kuruluyor. Mac için uygulanacak komutların listesi lib klasörü içinde


##Tradingview ve Python sinyal stratejisi
_______________________________________________________________
22102022-Kararlar
-sat verdiginde eger alim saatini x saat gecmemisse alt limite baksin eger gecmisse satsın ama eğer x saatini geçmişse kar orani 0.1'den buyukse alt bir limit beklemesin sat sinyaline bakmadan direk satsin cunku uzun surede zarar ediyor (x değeri marginlerde 2 saat, altcoinlerde 3 saat)
-sat i 60 dan 50 ye cek 
-kar icin beklenen alt limiti tüm robotlarda 1 e cek
-zarar icin stop u tüm robotlarda 1 e cek


SON GUNCELLEME - 20.10.2022 :  Yeni MarginBTC robotu
________________________
Alış
İf(son satışı zarar yapmamış ise 
  || zararına satış yapmışsa ve üzerine 6 saat geçmiş ise) 
    && 15dk-rsi da 25 altında al ise
    && aynı pozisyonda daha önceden 1 den fazla alınmamışsa yani aynı anda max 2 Trade olsn 
    

Satış
15dk-rsi da 50 üzerinde sat ama Robot sat verince satması için min %1 kar yapmış olması lazım

Robot %1 zararda stop olacak ve satacak

Robot %2.5 kar yapmışsa trailing başlatıp %0.5 ilk düştüğü anda satacak 


SON GUNCELLEME - 14.09.2022 : 
btc fiyatına göre ema 20 günlüğün fiyatı ema 50 günlük fiyatının altındaysa 
ve mevcut btc fiyatı ema 50 nin üzerine çıktıysa alış yapma


_______________________________________________________________
SON GUNCELLEME - 20.07.2022 : 

Robot15m ve RobotMargin için;
Yapılan : 4saatlik emanın üzerinde olursa satın al
İleride yapılabilecek : 1Günlük Ema kontrolüne ek olarak Btc 1Günlük rsi ı 40 den az ise alımlara izin ver

_______________________________________________________________

SON GUNCELLEME - 16.08.2022 : 
Robotlar 1günlük ema üzerinde alım yapacak, 1günlük ema'nın %10 altına düştüğünde stop olacak

_______________________________________________________________
SON GUNCELLEME - 20.07.2022 : 

+Margin için short alımı kapatıldı. (Önceden yapılmıştı)
+RSI_15_Robot'da ve margin_robot_long'da alım yaparken coinin hem btc hem de usdt karşısındaki değerine bakacak ve alım yapmak için bunlardan birisi min_rsi değeri altındayken diğerinin de rsi'ının 50 altında olması koşulu aranacak, satış yaparken de aynı şekilde hem btc hemde usdt ye bakacak
+%4 kar ettikten sonra tetiklenen ve %1 kaybedişinde satış yapar stoploss trigger i eklenip margin ve rsi15 robotlarına eklendi
_______________________________________________________________


YÜKLÜ => python 3.7.9 

Robot1 - RSI_4h:
+ALIŞ;
Altcoin/btc 30,60,120 lıklardan 1 tanesi ve 240 dk lık grafikte 20 altında ise  (yeni hali sadece 4 sa kontrol ediliyor)
ve hepsi 50 altında ise (yeni hali 30,1sa,4sa lik kontrol edilip 50 altında) 
ve btc/usdt wlliamR günlükte -50'den küçük ise al ,  
+SATIŞ;
Altcoin/btc 15,30,60,120 lıklardan 1 tanesi ve 240 dk lık grafikte 75 üzerinde ise  
ve hepsi 50 üzerinde ise 
Ve btc/usdt kar %2 üzerindeyse sat

Robot2 - RSI_15m:
ALIŞ; 15dk'ik Rsi 25'in altındaysa VE Btc Ema üzerindeyse al,  
SATIŞ; 15dk'ik Rsi 65'in üzerinde ise ve btc/usdt kar %2 üzerindeyse sat

Robot3 - Btc Margin 

ALIŞ; ema20d üzerindeyken sadece long, altındayken hem long hem short işlem açılır. Altcoin/btc 15dk'ik Rsi 25'in altındaysa al,  
SATIŞ; Altcoin/btc 15dk'ik Rsi 65'in üzerinde ise ve btc/usdt kar %2 üzerindeyse sat



Satış Modları : 
2 farklı satış stratejisi var.
1-) Hem manuel hem Rsi4h robotla alınanlar için uygulanan strateji olarak 2 katında yarısını ve sonraki 2 katlarında %10'u satılır. Minimum tutar a gelindiyse tamamı satılır
2-) Rsi15m ve Margin robotlarıyla alınanlarda sinyal gelmesi durumunda tamamı satılır.
Satış durumlarında Robot sinyali ile satış durumunda üzerinden 2 gün geçmeden tekrar satış yapılmaz

 Alış son onay : al sinyali verdiyse para birimi en son ne zaman alındı diye bakılır. son alımdan sonra 3 günden az süre geçtiyse veya Eğer son alım olduysa veya fark yukarı veya aşağı yönlü %5 ten az ise alınmayacak 

Satılan altcoinler ile usdt alınır. coinTargetToCollectbtc  seçili ise Btc için sinyal geldiğinde de kenardaki biriken usdt ile btc alınır.


Alım yaparken cd kontrolü yap. ilk alımda 1gün cd , 2.cide 2 , 3.cüde 3, 4cüde 4 gün cd ile geçtiğini kontrol et (cd gün sayısı = mevcut trade adeti * 2 )

