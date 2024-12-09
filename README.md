# Django Forms API

Этот проект представляет собой API на основе Django, который позволяет отправлять формы и обрабатывать их данные. API поддерживает различные типы форм, такие как регистрация пользователей, обратная связь и регистрация на мероприятия. Также в проекте интегрирован Swagger для удобного документирования и тестирования API.

## Содержание

- [Требования](#требования)
- [Установка](#установка)
- [Запуск проекта](#запуск-проекта)
- [Использование API](#использование-api)
- [Документация API с помощью Swagger](#документация-api-с-помощью-swagger)
- [Тестирование](#тестирование)

## Требования

- Docker
- Docker Compose
- Python 3.11
- Django 3.1
- Django REST Framework
- Djongo (для работы с MongoDB)

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone <URL_репозитория>
   cd <имя_папки_репозитория>
   ```
2. Убедитесь, что у вас установлен Docker и Docker Compose.
3. Установите зависимости, указанные в requirements.txt, с помощью Docker:
     ```bash
   docker-compose build
    ```
## Запуск проекта

1. Запустите контейнеры с помощью Docker Compose:
```bash
docker-compose up
```
2. После успешного запуска вы сможете получить доступ к API по адресу: http://localhost:8000/api/sendForm/.

## Использование API

API поддерживает следующие формы:

1. Регистрация пользователя
- URL: /api/sendForm/
- Метод: POST
- Тело запроса:
```json
    [
  {"name": "username", "value": "testuser"},
  {"name": "email", "value": "test@example.com"},
  {"name": "password", "value": "securepassword"},
  {"name": "confirm_password", "value": "securepassword"}
]
```

2. Обратная связь
- Тело запроса:
```json
[
  {"name": "email", "value": "feedback@example.com"},
  {"name": "rating", "value": "5"},
  {"name": "comments", "value": "Great service!"}
]
```
3. Регистрация на мероприятие
- Тело запроса:
```json
[
  {"name": "event_name", "value": "Tech Conference"},
  {"name": "date", "value": "2024-05-01"},
  {"name": "attendee_email", "value": "attendee@example.com"},
  {"name": "phone", "value": "+79001234567"}
]
```

### Примеры запросов
Вы можете использовать curl или Postman для отправки запросов к API. Пример с использованием curl:
```bash
curl -X POST http://localhost:8000/api/sendForm/ -H "Content-Type: application/json" -d '[
  {"name": "username", "value": "testuser"},
  {"name": "email", "value": "test@example.com"},
  {"name": "password", "value": "securepassword"},
  {"name": "confirm_password", "value": "securepassword"}
]'
```

## Документация API с помощью Swagger
Swagger интегрирован в проект для удобного документирования и тестирования API. Вы можете получить доступ к интерфейсу Swagger по следующему адресу:
- http://localhost:8000/swagger/

Здесь вы сможете просмотреть доступные эндпоинты, их параметры и тестировать API прямо из браузера.

## Тестирование

Для запуска тестов выполните следующую команду:

```bash
docker-compose run test
```
Это выполнит миграции, заполнит базу данных тестовыми данными и запустит тесты.
