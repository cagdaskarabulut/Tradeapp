# TRADEAPP

## Python, django teknolojileri ile geliştirilmiş celery ile periodik olarak otomatik çalışarak belirli algoritmalara göre alım/satım yaparn Binance ile entegre çalışan trade uygulamasıdır.

### Çalıştırmak için 4 farlı terminal sayfasında venv aktive edip aşağıdaki komutlar herbir terminal ekranında çalıştırılır
1- python manage.py runserver 127.0.0.1:8000
2- redis-server
3- celery -A trade worker -l INFO
4- celery -A trade beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

