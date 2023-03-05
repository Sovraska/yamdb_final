# Yamdb_final  CI/CD 

## Технологический стек
[![yamdb_final](https://github.com/sovraska/yamdb_final/actions/workflows/.github/workflows/main.yml/badge.svg)]
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=008080)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=56C0C0&color=008080)](https://www.postgresql.org/)
[![JWT](https://img.shields.io/badge/-JWT-464646?style=flat&color=008080)](https://jwt.io/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat&logo=NGINX&logoColor=56C0C0&color=008080)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=56C0C0&color=008080)](https://gunicorn.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker-compose](https://img.shields.io/badge/-Docker%20compose-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker Hub](https://img.shields.io/badge/-Docker%20Hub-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/products/docker-hub)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat&logo=GitHub%20actions&logoColor=56C0C0&color=008080)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat&logo=Yandex.Cloud&logoColor=56C0C0&color=008080)](https://cloud.yandex.ru/)
Этот **Backend** Создан для Взаимодействия с **Frontend** частью Проекта.  

В основном он нужен для обращения к **базе данных** И получения нужной информации.

Он может пригодиться тем кто не хочет писать backend  
а сразу хочет потренировать свои навыки во **Frontend** :smile:




# Как запустить проект:
Клонируйте репозиторий `git@github.com:Sovraska/infra_sp2.git`

- Создайте `.env` файл в директории `infra/`, в котором должны содержаться следующие переменные:
 
    >DB_ENGINE=django.db.backends.postgresql\
    DB_NAME= # название БД\ 
    POSTGRES_USER= # ваше имя пользователя\
    POSTGRES_PASSWORD= # пароль для доступа к БД\
    DB_HOST=db\
    DB_PORT=5432\

- Из папки `infra/` соберите образ при помощи docker-compose
`$ docker-compose up -d --build`


- Примените миграции
`$ docker-compose exec web python manage.py migrate`


- Соберите статику
`$ docker-compose exec web python manage.py collectstatic --no-input`


- Для доступа к админке не забудьте создать суперюзера  
`$ docker-compose exec web python manage.py createsuperuser`


- Что бы Можно было протестировать работу Предлагаем вам Установить Фикстуры  
`$ docker-compose exec web python manage.py loaddata fixtures.json`

# Где Можно Посмотреть на примеры запросов к API ?
Например, после запуска проекта можно посмотреть [Документацию](http://127.0.0.1:8000/redoc/).

Но я приведу несколько примеров.

POST http://127.0.0.1:8000/api/v1/auth/signup/  
<sub>Регистрация Пользователя </sub>

    {
        "username":"Fake",
        "email": "Fake.fake@gmail.com"
    }

POST http://127.0.0.1:8000/api/v1/auth/token/        
в бэк приходит письмо с кодом  
<sub>Получение Jwt Токена</sub>

    {
        "username":"Fake",
        "confirmation_code": "biv4hr-69c31c5b2ad53627baf8c1f5273156e3"
    }

POST http://127.0.0.1:8000/api/v1/titles/1/reviews/1/comments/1/ 
<sub>Оставить комментарий для</sub>  
<sub>произведения с id=1</sub>  
<sub>ревью id=1</sub>  
<sub>Коммента id=1</sub>  

    {
        "text": "testComment"
    }

POST http://127.0.0.1:8000/api/v1/auth/users/me/
в бэк приходит письмо с кодом  
<sub>Получение Jwt Токена</sub>

    {
        "username": "Fake",
        "email": "Fake.fake@gmail.com",
        "first_name": "",
        "last_name": "",
        "bio": "",
        "role": "user"
    }

# Над Проектом Трудились
- [Новиков Семён](https://github.com/Sovraska) - Архитектура проекта, API регистрации и авторизации пользователей, контейнеризация
- [Чебан Илья](https://github.com/Ilya-Cheb0503) - API Жанров, Категорий и Произведений
- [Сергей Скляр](https://github.com/XDreamsonX) - Api Ревью и Комментариев
