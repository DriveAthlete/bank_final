1. активировать venv https://tyapk.ru/blog/post/python-virtual-environment-windows
2. установить все зависимости pip install -r req.txt
3. настроить базу данных postgresql 
4. указать данные для подключения к базе данных в файле settings.py 
```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'bank_final',
            'USER': 'bank',
            'PASSWORD': '12345',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
```
5. провести миграции `python manage.py migrate`
6. запустить приложение `python manage.py runserver`