# Проект "Сервис покупки товаров для авторизованных пользователей"

### Направление: Async
Теги: Git, JWT, ORM, OpenApi Docs, PEP8, Readme, Tests, Auth, Docker, Docker-Compose,
Async, FastAPI, SQL Alchemy

Модули: fastapi, pydantic, pydantic-settings, sqlalchemy, alembic, asyncpg
---
## Содержание:

---
## Структура проекта:
```
TA4/
├── app/
|   ├── migtrate # миграции
|   |   ├── versions # версии миграций
|   |   |   └── ...
|   |   ├── __init__.py
|   |   ├── env.py
|   |   ├── README
|   |   └── script.py.mako
|   ├── users # директория пользователей
|   |   ├── __init__.py
|   |   ├── models.py
|   |   ├── routers.py
|   |   └── schemas.py
|   ├── products # директория товаров
|   |   ├── __init__.py
|   |   ├── models.py
|   |   ├── routers.py
|   |   └── schemas.py
|   ├── __init__.py
|   ├── config.py # настройка приложения
|   ├── database.py # настройка подключения к БД
|   └── main.py
├── .env
├── .flake8 # настройка для flake8
├── .gitignore
├── poetry.lock
├── alembic.ini # настройка alembic
├── pypproject.toml # зависимости для poetry
└── README.md

```

└── requirements.txt # зависимости для pip

## APP
---
## Модели:
- ### Users:
    Модель пользователей:
  - id: int - PK
  - full_name: str - ФИО
  - email: str - электронная почта
  - phone: str - мобильный номер телефона
  - password: str - пароль

- ### Products:
    Модель товаров:
  - id: int - PK
  - name: str - название
  - price: int - цена
  - created_at: datetime - дата создания
  - updated_at: datetime - дата обновления
  - is_active: boll - активное

---
## Схемы:
- ### UserCreate:
    Схема для создания пользователя:
  - full_name: ФИО пользователя.
  - email: Адрес электронной почты.
  - phone: Номер телефона, должен соответствовать:
  - должен начинаться на +7 и содержать 10 цифр
  - password: Пароль, должен соответствовать:
    - не менее 8 символов;
    - только латинские буквы;
    - минимум 1 заглавная буква;
    - минимум 1 строчные буква;
    - минимум 1 спец символы ($%&!:).
  - confirm_password: Подтверждение пароля.
---
## Ручки:
