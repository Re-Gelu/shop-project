# :poop: Интернет-маркетплейс на Django
> Pet-проект. Создается в целях более лучшего изучения Django :shipit:

## :memo: [Changelog](https://github.com/Re-Gelu/Sample_shop/blob/master/changelog.txt)

## :triangular_ruler: Стек проекта: 
- Python 3.11 (Django, Django REST framework, Celery)
- HTML5, CSS (Bootstrap 5, UIkit), JS (Next.js, React, jQuery)
- NGNIX, Gunicorn
- Redis, PostgreSQL

## :package: [Зависимости бекэнда](https://github.com/Re-Gelu/Shop-project/blob/master/requirements.txt)
## :package: [Зависимости фронтенда](https://github.com/Re-Gelu/Shop-project/blob/master/frontend/package.json)

## :wrench: Запуск проекта

- Создаём виртуальное окружение Python и активируем его

  ```
  $ python -m venv venv
  $ venv\Scripts\activate.bat - для Windows / source venv/bin/activate - для Linux и MacOS
  ```

- Устанавливаем зависимости проекта

  ```
  $ pip install -r requirements.txt
  ```
  
- Создаем кеш-таблицу в бд (нужна для хранения настроек проекта)

  ```
  $ python manage.py createcachetable
  ```

- Выполняем миграции бд

  ```
  $ python manage.py migrate --noinput
  ```
  
- Обычный запуск

  ```
  $ python manage.py runserver
  ``` 

- Запуск при помощи Gunicorn

  ```
  $ gunicorn config.wsgi:application --bind 0.0.0.0:8000
  ```
  
> И определенно стоит настроить .env файл перед запуском


## :whale: Работа с Docker

- Собрать проект (prod.env или dev.env)
  ```
  $ docker-compose -f docker-compose.yml up -d --build
  ```

- Удаление контейнеров

  ```
  $ docker-compose down -v
  ```

## :closed_lock_with_key: Настройка входа в админку

```
$ python manage.py createsuperuser --username admin@email.com --email admin@email.com
```
```
$ docker-compose -f docker-compose.yml exec web python manage.py createsuperuser --username admin@email.com --email admin@email.com
```

## :moneybag: Оплата

Реализована при помощи QIWI API, проверка оплаты происходит при помощи задач Celery по расписанию.

Требуется обязательно установить приватный ключ QIWI в админке или settings.py / .env файлах.
Получить можно тут: https://qiwi.com/p2p-admin/api

- Команды Celery 

  ```
    Windows:
  $ celery -A config beat --loglevel=info
  $ celery -A config worker --pool=solo --loglevel=info
  
    Linux:
  $ celery -A config worker --beat --loglevel=info
  ```
  
## :sleeping: REST API

Полный REST API, пригодится когда буду заниматься выделенным фронтом. Для доступа к некоторым разделам API нужны права администратора.
API swagger:  ```http://.../swagger``` 

## :black_nib: Авто-заполнение магазина для быстрого тестирования

POST запрос по адресу ```http://.../api/db_auto_fill``` с содержимым в формате:

```
{
  model: "Categories",
  amount: 7
}
```

> Необходимы права администратора
  
## :camera: Скрины проекта
![Изображение №1](https://user-images.githubusercontent.com/75813517/199733106-cda4086c-11d1-431b-a853-0b00bdeb165f.png)
![Изображение №2](https://user-images.githubusercontent.com/75813517/199733450-389a54c8-18d5-4f43-b9c8-ddaeab7486c9.png)
![Изображение №3](https://user-images.githubusercontent.com/75813517/199733692-bf94269c-043a-45d9-818a-8430408c75e7.png)
![Изображение №4](https://user-images.githubusercontent.com/75813517/199733891-7cf053ef-2f34-43bb-bb8e-d247c6f5ba80.png)
![Изображение №5](https://user-images.githubusercontent.com/75813517/199734053-debf4bfa-14cd-4771-9414-af2f56fe2bc6.png)
![Изображение №6](https://user-images.githubusercontent.com/75813517/199734154-a2008491-838e-4af6-96a8-0775d38821c8.png)
![Изображение №7](https://user-images.githubusercontent.com/75813517/199734251-e7d27528-c5ac-4bb0-9a61-b8c290af1232.png)
![Изображение №8](https://user-images.githubusercontent.com/75813517/214181643-c3f95e35-616a-4281-b875-a4c10def33be.png)
![Изображение №9](https://user-images.githubusercontent.com/75813517/214181841-eb8f48de-13cf-4b59-a10d-e1a7e7da467e.png)



