# Проект: Домашняя работа 1

## Задача
Реализовать сервис, который пройдет проверки из этого репозитория: [qa_guru_python_9_19](https://github.com/qa-guru/qa_guru_python_9_19/blob/master/test_reqres.py).

## Что было сделано
Было реализовано два эндпоинта, различаются логикой и методом HTTP-запроса. Подробности описаны ниже.

### Эндпоинты

1. **GET /api/users**
   - **Описание**: Этот эндпоинт может принимать параметры `?page=1&per_page=2`.
   - **Результат**: Возвращает список пользователей в формате `dict`.

   **Пример запроса**:
GET /api/users?page=1&per_page=2

**Пример ответа**:
```json
{
    "data": [
        {
            "id": 1,
            "email": "george.bluth@reqres.in",
            "first_name": "George",
            "last_name": "Bluth",
            "avatar": "https://reqres.in/img/faces/1-image.jpg"
        },
        {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        }
    ],
    "page": 1,
    "per_page": 2,
    "total": 12,
    "total_pages": 6
}
```

2. **POST /api/users**
    - **Описание**: Этот эндпоинт требует request_payload в виде:
```json
{
    "name": "asdf",
    "job": "asdff"
}
```

 - **Результат**: Возвращает dict созданного пользователя (на самом деле пользователь не создается).

**Пример запроса**:
```text
POST /api/users
Content-Type: application/json

{
    "name": "asdf",
    "job": "asdff"
}
```

**Пример ответа**:
```json
{
    "name": "asdf",
    "job": "asdff",
    "id": 1,
    "createdAt": "2024-07-20T06:41:57.327Z"
}
```

**Установка**

Клонируйте репозиторий:
```bash
git clone <URL этого репозитория>
```

Перейдите в директорию проекта:
```bash
cd <имя директории куда скачали репозиторий>
```

Установите необходимые зависимости:
```bash
pip install -r requirements.txt
```

**Запуск**

Чтобы запустить сервис, выполните команду:
```bash
uvicorn main:app --host=127.0.0.1 --port=8002 --reload
```
Проверялся запуск на windows, как на других ОС работает не проверял

**Тестирование**

Для запуска тестов используйте:
Перед тем как запустить тесты откройте новую console, чтобы там ввести эту команду
```bash
pytest ./tests.py
```
