![example workflow](https://github.com/catstyle1101/recipe_collection/actions/workflows/foodgram_workflow.yml/badge.svg)
# Recipe collection - сборник рецептов приготовления блюд.

доступен по адресу: http://catstyle.ddns.net


## Возможности
- Размещать рецепты на сайте
![image](https://github.com/catstyle1101/recipe_collection/assets/37059480/d90144f6-7776-461b-a70b-f8dd55ae8fbf)
- У рецептов есть теги (завтрак, обед, ужин, можно добавлять свои)
- У рецептов есть ингредиенты (база с более 2 тысяч ингредиентов заливается автоматически).
- К рецептам необходимо прикреплять фотографии
- Есть возможность подписываться на авторов и добавлять рецепты в избранное
![image](https://github.com/catstyle1101/recipe_collection/assets/37059480/e4bacef3-ee8f-4043-bdc2-316b19f6e1d1)
- Есть возможность добавлять рецепты в корзину и скачивать ингредиенты, как список покупок
![image](https://github.com/catstyle1101/recipe_collection/assets/37059480/de249d51-6ffd-4ac6-be33-f494ee0e797a)
- Реализована панель администратора для управления сайтом. доступна по адресу http://<your_address>/admin/
![image](https://github.com/catstyle1101/recipe_collection/assets/37059480/0e4a15bc-3d4a-4d6a-b1d9-f14b5abeeca7)


## Пользовательские роли и права доступа
- Гость (неавторизованный пользователь)
- Авторизованный пользователь
- Администратор

## Stack
- Python 3.11
- Django 4.2
- DRF 3.14
- Docker
- Nginx
- Postgresql

## Запуск
- Склонировать репозиторий
```git clone git@github.com:catstyle1101/recipe_collection.git```
- Подключиться к серверу
```ssh <user>@<server_ip>```
- Установить Docker и docker-compose на сервер
```
sudo apt install docker.io
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
mkdir foodgram && cd foodgram/
```
- Создать файл .env с содержимым
```
touch .env

SECRET_KEY=<secret_key>
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<postgre_password>
DB_HOST=db
DB_PORT=5432
```
- Скопировать папку infra на сервер
```
scp -r infra/* <user>@<server_ip>:/home/<user>/foodgram/
```
- Запустить docker-compose
```
sudo docker-compose up -d
```

## Создание суперпользователя

```
sudo docker exec -it foodgram_backend_1 bash

python manage.py createsuperuser
```


## Документация по проекту

Доступна по адресу http://<your_address>/api/redoc/
