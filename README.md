t# Foodgram - сборник рецептов.

## Возможности
- Размещать рецепты на сайте 
- У рецептов есть теги (завтрак, обед, ужин)
- У рецептов есть ингредиенты.
- К рецептам необходимо прикреплять фотографии
- Есть возможность подписываться на авторов и добавлять рецепты в избранное
- Есть возможность добавлять рецепты в корзину и скачивать ингредиенты, как список покупок

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
```git clone git@github.com:catstyle1101/foodgram-project-react.git```
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

SECRET_KEY=<Your_some_long_string>
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<Your_password>
DB_HOST=db
DB_PORT=5432
```
- Скопировать папку infra на сервер
```
scp -r infra/* <server user>@<server IP>:/home/<server user>/foodgram/
```
- Запустить docker-compose
```
sudo docker-compose up -d
```
