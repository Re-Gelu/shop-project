# :poop: Интернет-маркетплейс на Django
> Pet-проект. Создается в целях более лучшего изучения Django :shipit:

## :memo: [Changelog](https://github.com/Re-Gelu/Sample_shop/blob/master/changelog.txt)

## :triangular_ruler: Стек проекта: 
- Python 3.11 (Django, Django REST framework, Celery)
- HTML5, CSS (Bootstrap 5, UIkit), JS (jQuery)
- NGNIX, Gunicorn
- Redis, PostgreSQL

## :package: [Зависимости проекта](https://github.com/Re-Gelu/Sample_shop/blob/master/requirements.txt)

## :closed_lock_with_key: Настройка входа в админку

```
$ python manage.py createsuperuser --username admin --email admin@email.com
```
```
$ docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser --username admin@email.com --email admin@email.com
```

## :black_nib: Авто-заполнение магазина для быстрого тестирования

```
http://.../db_auto_fill/7/Categories/
```
```
http://.../db_auto_fill/10/Subcategories/
```
```
http://.../db_auto_fill/300/Products/
```

> Необходимы права администратора

## :moneybag: Оплата

Реализована при помощи QIWI, проверка оплаты происходит при помощи задач Celery по расписанию.

Требуется обязательно установить приватный ключ QIWI в админке или settings.py / .env файлах.
Получить можно тут: https://qiwi.com/p2p-admin/api

- Команды Celery 

  ```
    Windows:
  $ celery -A Site beat --loglevel=info
  $ celery -A Site worker --loglevel=info /  $ celery -A Site worker --pool=solo --loglevel=info
  
    Linux:
  $ celery -A Site worker --beat --loglevel=info
  ```

## :whale: Работа с Docker

- Удаление контейнеров

  ```
  $ docker-compose down -v
  ```

- Поднять Prod контейнер
  ```
  $ docker-compose -f docker-compose.prod.yml up -d --build
  ```
  
## :sleeping: REST API

Сделан небольшой REST API, мб пригодится. Для доступа к некоторым разделам API нужны права администратора.

![REST API](https://user-images.githubusercontent.com/75813517/205884672-97a00e2e-3978-49ce-a769-faef4479ddbc.png)

  
## :camera: Скрины проекта
![Изображение №1](https://user-images.githubusercontent.com/75813517/199733106-cda4086c-11d1-431b-a853-0b00bdeb165f.png)
![Изображение №2](https://user-images.githubusercontent.com/75813517/199733450-389a54c8-18d5-4f43-b9c8-ddaeab7486c9.png)
![Изображение №3](https://user-images.githubusercontent.com/75813517/199733692-bf94269c-043a-45d9-818a-8430408c75e7.png)
![Изображение №4](https://user-images.githubusercontent.com/75813517/199733891-7cf053ef-2f34-43bb-bb8e-d247c6f5ba80.png)
![Изображение №5](https://user-images.githubusercontent.com/75813517/199734053-debf4bfa-14cd-4771-9414-af2f56fe2bc6.png)
![Изображение №6](https://user-images.githubusercontent.com/75813517/199734154-a2008491-838e-4af6-96a8-0775d38821c8.png)
![Изображение №7](https://user-images.githubusercontent.com/75813517/199734251-e7d27528-c5ac-4bb0-9a61-b8c290af1232.png)
![Изображение №8](https://user-images.githubusercontent.com/75813517/199734371-bec5cfc7-9a35-4011-8af7-5e70a798f8c2.png)
![Изображение №9](https://user-images.githubusercontent.com/75813517/199734488-5ae111bf-a545-4282-bed3-4ca41206a0ec.png)



