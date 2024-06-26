# api_final
api final - это законченная версия API для социальной сети Yatube. Через этот интерфейс смогут работать мобильное приложение или чат-бот; через него можно будет передавать данные в любое приложение или на фронтенд.

Для аутентификации авторизованных пользователей используются JWT-токены.

Функциональные возможности социальной сети Yatube - авторизованные пользователи могут публиковать посты и изменять или удалять контент, авторами которых они являются; оставлять комментарии и удалять их под своими постами и постами других авторов, а так же подписываться или отписываться от авторов. Для неавторизованных пользователей доступен режим "только чтение", они не могут создать/изменить/удалить контент.

Используемый стек технологий:
Python 3.8.9,
Django 3.2.16, 
DRF, 
JWT + Djoser.

Чтобы запустить локально, нужно:

1.Клонировать репозиторий, перейти в директорию с проектом.

2.Создать и активировать виртуальное окружение:

python -m venv venv 

source venv/Scripts/activate

3.Установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip

pip install -r requirements.txt

4.Выполнить миграции:

python yatube_api/manage.py migrate

5.Запустить проект:

python yatube_api/manage.py runserver

После запуска проекта на сервере по адресу http://127.0.0.1:8000/redoc/ будет доступна документация для API Yatube.
В документации описано, как должен работать API.

Примеры работы с API для всех пользователей

Для неавторизованных пользователей работа с API доступна в режиме чтения, что-либо изменить или создать не получится.

GET api/v1/posts/ - получить список всех публикаций. 

При указании параметров limit и offset выдача должна работать с пагинацией 
GET api/v1/posts/{id}/ - получение публикации по id 

GET api/v1/groups/ - получение списка доступных сообществ 

GET api/v1/groups/{id}/ - получение информации о сообществе по id 

GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации 

GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id


Примеры работы с API для авторизованных пользователей

Для создания публикации используем:

POST /api/v1/posts/

в body

{
"text":
"string",
"image": 
"string", 
"group": 0 
}

Обновление публикации:

PUT /api/v1/posts/{id}/

в body

{
    "text": 
    "string", 
    "image": 
    "string", 
    "group": 0 
    }

Частичное обновление публикации:

PATCH /api/v1/posts/{id}/

в body

{
    "text": 
    "string", 
    "image": 
    "string", 
    "group": 0 
    }


Частичное обновление публикации:

DEL /api/v1/posts/{id}/

Получение доступа к эндпоинту /api/v1/follow/ (подписки) доступен только для авторизованных пользователей.

Подписка пользователя, от имени которого сделан запрос на пользователя переданного в теле запроса.

GET /api/v1/follow/

Анонимные запросы запрещены.

Добавить группу в проект нужно через админ панель Django:

После авторизации, переходим в раздел Groups и создаем группы.

admin/

Доступ авторизованным пользователем доступен по JWT-токену (Joser), который можно получить выполнив POST запрос по адресу:

POST /api/v1/jwt/create/

Передав в body данные пользователя (например в postman):

{
    "username": 
    "string", 
    "password": 
    "string" 
    }


Полученный токен добавляем в headers (postman), после чего буду доступны все функции проекта:

Authorization: Bearer {your_token}

Обновить JWT-токен:

POST /api/v1/jwt/refresh/

Проверить JWT-токен:

POST /api/v1/jwt/verify/

В проекте API реализована пагинация (LimitOffsetPagination):

GET /api/v1/posts/?limit=5&offset=0


Автор - Тарасова Евгения.