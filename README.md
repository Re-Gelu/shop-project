# :poop: Интернет - маркетплейс на Django
> Проект создается в целях изучения Django для портфолио :shipit:

## :white_circle: Стек проекта: 
- Python (Django, Django REST)
- HTML5
- CSS (Bootstrap 5, UIkit)
- NGNIX, Gunicorn

## :memo: [Changelog](https://github.com/Re-Gelu/Sample_shop/blob/master/changelog.txt)

## :closed_lock_with_key: Админка

- Логин: *admin*
- Пароль: *1234*

> Либо python manage.py createsuperuser admin 1234 --noinput

## :white_circle: Авто-заполнение магазина для быстрого тестирования

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
