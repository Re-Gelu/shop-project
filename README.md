# :poop: Интернет-маркетплейс на Django
> Проект создается в целях изучения Django для портфолио :shipit:

## :memo: [Changelog](https://github.com/Re-Gelu/Sample_shop/blob/master/changelog.txt)

## :triangular_ruler: Стек проекта: 
- Python (Django, Django REST)
- HTML5
- CSS (Bootstrap 5, UIkit)
- NGNIX, Gunicorn
- Celery, Redis

## :package: Зависимости проекта
```
Django==4.0.8
djangorestframework==3.13.1
django-filter==22.1
FileBrowser==1.1.3
django-filebrowser-no-grappelli==4.0.1
django-tinymce==3.5.0
django-admin-interface==0.20.0
django-extra-settings==0.6.1
django-phonenumber-field[phonenumbers]==7.0.0
celery==5.2.7
django-celery-results==2.4.0
django-celery-beat==2.3.0
redis==4.3.4
pyQiwiP2P==2.0.6
shortuuid==1.0.9
Markdown==3.4.1
psycopg2-binary==2.9.3
Pillow==9.2.0
gunicorn==20.1.0
art==5.7
pytz==2022.4
tzdata==2022.5
```

## :closed_lock_with_key: Настройка входа в админку

- `$ python manage.py createsuperuser --username admin --email admin@email.com`
- `$ docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser --username admin --email admin@email.com`

## :black_nib: Авто-заполнение магазина для быстрого тестирования

```
.../db_auto_fill/7/Categories/
```
```
.../db_auto_fill/10/Subcategories/
```
```
.../db_auto_fill/300/Products/
```

> Необходимы права администратора

## :whale: Работа с Docker

- rm containers

  ```
  $ docker-compose down -v
  ```

- Dev
  ```
  $ docker-compose -f docker-compose.yml up -d --build
  ```

- Prod
  ```
  $ docker-compose -f docker-compose.prod.yml up -d --build
  $ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
  $ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
  ```
  
## :camera: Скрины проекта

![Изображение №1](https://user-images.githubusercontent.com/75813517/188868325-ccd04c10-ce03-4f4e-953d-585486d8c895.png)
![Изображение №2](https://user-images.githubusercontent.com/75813517/188868290-8b498777-60ec-4122-b541-f212753966cc.png)
![Изображение №3](https://user-images.githubusercontent.com/75813517/188868272-d8536fb7-d3bc-4877-baf1-665ba7183fcd.png)
![Изображение №4](https://user-images.githubusercontent.com/75813517/188868235-59a80095-d2be-474e-849c-b36b1562ce31.png)
![Изображение №5](https://user-images.githubusercontent.com/75813517/188868163-d8e8793e-85f7-467a-9378-000430b886c1.png)
