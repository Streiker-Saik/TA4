# Проект "Сервис покупки товаров для авторизованных пользователей"

### Направление: Async
Теги: Git, JWT, ORM, OpenApi Docs, PEP8, Readme, Tests, Auth, Docker, Docker-Compose,
Async, FastAPI, SQL Alchemy

Модули: fastapi, pydantic, pydantic-settings, sqlalchemy, alembic, asyncpg, pyjwt, passlib, uvicorn

---
## Содержание:
- [Проверить версию Python](#проверить-версию-python)
- [Установка Poetry](#установка-poetry)
- [Установка приложения](#установка-приложения)
  - [При использовании PIP](#при-использовании-PIP)
  - [При использовании POETRY](#при-использовании-POETRY)
- [Структура проекта](#структура-проекта)
- [Services](#services)
  - [Основа](#основа)
    - [BaseService](#baseservice)
- [Users](#users)
  - [Модели Users](#модели-users)
    - [User](#user)
  - [Сервис Users](#сервис-users)
    - [ProductService](#ProductService)
  - [Схемы Users](#схемы-users)
    - [SUserRegister](#SUserRegister)
    - [SUserLogin](#SUserLogin)
- [Products](#products)
  - [Модели Products](#модели-Products)
    - [Product](#Product)
  - [Сервис Products](#сервис-Products)
    - [UserService](#UserService)
  - [Схемы Products](#схемы-Products)
    - [SProductCreate](#SProductCreate)
    - [SProductResponse](#SProductResponse)
    - [SProductUpdate](#SProductUpdate)

---
## Проверить версию Python:

Убедитесь, что у вас установлен Python (версия 3.x). Вы можете проверить установленную версию Python, выполнив команду:
```
python --version
```

[<- на начало](#содержание)

---
## Установка Poetry:
- Если у вас еще не установлен Poetry, вы можете установить его, выполнив следующую команду
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
- Проверить Poetry добавлен в ваш PATH.
    ```bash
    poetry --version
    ```

[<- на начало](#содержание)

---
## Установка приложения:
- Клонируйте репозиторий:
    ```bash
    git clone git@github.com:Streiker-Saik/TA4.git
    ```
- Перейдите в директорию проекта:
    ```
    cd TA4
    ```
- ### При использовании PIP:
  - Активируйте виртуальное окружение
      ```
      python -m venv <имя_вашего окружения>
      <имя_вашего_окружения>\Scripts\activate
      ```
  - Установите зависимости
      ```bash
      pip install -r requirements.txt
      ```
- ### При использовании POETRY:
  - Активируйте виртуальное окружение
      ```bash
      poetry shell
      ```
  - Установите необходимые зависимости:
      ```bash
      poetry install
      ```
  - Зайдите в файл .env.example и следуйте инструкция

[<- на начало](#содержание)

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
|   |   ├── schemas.py
|   |   └── service.py
|   ├── services # директория сервисов
|   |   ├── __init__.py
|   |   ├── base.py
|   ├── products # директория товаров
|   |   ├── __init__.py
|   |   ├── models.py
|   |   ├── routers.py
|   |   ├── schemas.py
|   |   └── service.py
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
├── README.md
└── requirements.txt # зависимости для pip
```

[<- на начало](#содержание)

---
## Services:
- ### Основа:
  - #### BaseService:
    Базовый сервис запросов к БД

[<- на начало](#содержание)

---
## Users:
- ### Модели Users:
  - #### User:
      Модель пользователей:
    - id: int - PK
    - full_name: str - ФИО
    - email: str - электронная почта
    - phone: str - мобильный номер телефона
    - password: str - пароль
    - is_admin: bool - администратор/пользователь
- ### Сервис Users:
  - #### ProductService:
    Родительский класс: **BaseService**  
    Сервис работы с продуктом в БД
- ### Схемы Users:
  - #### SUserRegister:
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
  - ### SUserLogin:
    Схема для авторизации пользователя
    - email: Адрес электронной почты
    - phone: Номер телефона
    - password: Пароль.

[<- на начало](#содержание)

---
## Products:
- ### Модели Products:
  - #### Product:
      Модель товаров:
    - id: int - PK
    - name: str - название
    - price: int - цена
    - created_at: datetime - дата создания
    - updated_at: datetime - дата обновления
    - is_active: boll - активное/не активное
- ### Сервис Products:
  - #### UserService:
    Родительский класс: **BaseService**  
    Сервис работы с пользователями в БД
- ### Схемы Products:
  - #### SProductCreate:
    Схема для создания продукта
    - name: Название
    - price: Цена
  - #### SProductResponse:
    Схема получение информации о продукте
    - id: id продукта
    - name: Название
    - price: Цена
    - create_at: Дата и время создания
    - updated_at: Дата и время изменения
    - is_active: Активное/не активное
  - #### SProductUpdate:
    Схема изменения информации о продукте
    - name: Название
    - price: Цена
    - is_active: Активное/не активное

[<- на начало](#содержание)

---
