# api_final
api final - это законченная версия API для социальной сети Yatube. Через этот интерфейс смогут работать мобильное приложение или чат-бот; через него можно будет передавать данные в любое приложение или на фронтенд. 
Автор - Тарасова Евгения.

Чтобы запустить локально, нужно:

Клонировать репозиторий, перейти в директорию с проектом.

Создать и активировать виртуальное окружение:
python -m venv venv source venv/Scripts/activate

Установить зависимости из файла requirements.txt:
python -m pip install --upgrade pip 
pip install -r requirements.txt

Выполнить миграции:
python yatube_api/manage.py migrate

Запустить проект:
python yatube_api/manage.py runserver
