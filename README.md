# YaCut

## О проекте

Проект YaCut — это сервис для сокращения длинных ссылок. Он позволяет связать длинную ссылку пользователя с короткой, которую пользователь может предложить сам или которую предоставит сервис.

## API для проекта
API доступен для всех желающих! Он поддерживает два основных эндпоинта:

### Создание короткой ссылки:

* /api/id/ — POST-запрос
```
    {
      'url': 'string',
      'custom_id': 'string'
    }
    ```

Используйте этот запрос для создания новой короткой ссылки.

### Получение оригинальной ссылки:

* /api/id/<short_id>/ - GET-запрос
```
    GET /api/id/{short_id}/
```

Запрос на получиние исходной  ссылки по указанному короткому идентификатору.

## Стек использованных технологий
* Python
* Flask
* Flask-SQLAlchemy
* HTML


## Разворачиваем проект.

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:Saida3232/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создайте файл .env и занесите в него нужные переменные.Например:

```
FLASK_APP=yacut
FLASK_DEBUG=1 # дебаг включен

SECRET_KEY =your_secret_key
DATABASE_URI =sqlite:///db.sqlite3

```

Запустить проект 

```
flask run
```


## Автор
Автор: [Saida](https://github.com/Saida3232)