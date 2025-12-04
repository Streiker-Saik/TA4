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
- [Auth](#Auth)
  - [Функции авторизации Auth](#функции-авторизации-Auth)
  - [Зависимости Auth](#зависимости-Auth)
  - [Маршруты Auth](#маршруты-Auth)
  - [Схемы Auth](#схемы-Auth)
    - [SUserRegister](#SUserRegister)
    - [SUserLogin](#SUserLogin)
- [Users](#users)
  - [Модели Users](#модели-Users)
    - [User](#user)
  - [Сервис Users](#сервис-users)
    - [UserService](#UserService)
- [Products](#products)
  - [Модели Products](#модели-Products)
    - [Product](#Product)
  - [Маршруты Products](#маршруты-Products)
  - [Схемы Products](#схемы-Products)
    - [SProductCreate](#SProductCreate)
    - [SProductResponse](#SProductResponse)
    - [SProductUpdate](#SProductUpdate)
  - [Сервис Products](#сервис-Products)
    - [ProductService](#ProductService)

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
|   |   ├── auth.py
|   |   ├── dependencies.py
|   |   ├── models.py
|   |   ├── routers.py
|   |   ├── schemas.py
|   |   └── service.py
|   ├── __init__.py
|   ├── config.py # настройка приложения
|   ├── database.py # настройка подключения к БД
|   ├── exceptions.py # ошибки
|   └── main.py
├── .env
├── .env.example # шаблон для создания .env
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
  Файл: [base.py](app/services/base.py)
  - #### BaseService:
    Базовый сервис запросов к БД

[<- на начало](#содержание)

---
## Auth:
- ### Функции авторизации Auth:
  Файл: [auth.py](app/auth/auth.py)
  - get_password_hash - Получение хэшированного пароля
  - verify_password - Проверка пароля
  - create_access_token - Создание токена 
  - authenticate_user **(async)** - Аутентификация пользователя
- ### Зависимости Auth:
  Файл: [dependencies.py](app/auth/dependencies.py)
  - get_token - Получение токена с **cookies**
  - get_current_user - Проверка авторизованного пользователя
  - get_current_user_is_admin - Проверка пользователя с правами администратора
- ### Маршруты Auth:
  Файл: [routers.py](app/auth/routers.py)
  - http://127.0.0.1:8000/auth/register
  **(POST)** Регистрация пользователя
  - http://127.0.0.1:8000/auth/login
  **(POST)** Авторизация пользователя
- ### Схемы Auth:
  Файл: [schemas.py](app/auth/schemas.py)
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
    Сервис работы с продуктом в БД

[<- на начало](#содержание)

---
## Users:
- ### Модели Users:
  Файл: [models.py](app/users/models.py)
  - #### User:
      Модель пользователей:
    - id: int - PK
    - full_name: str - ФИО
    - email: str - электронная почта
    - phone: str - мобильный номер телефона
    - password: str - пароль
    - is_admin: bool - администратор/пользователь
- ### Сервис Users:
  Файл: [services.py](app/users/services.py)  
  - #### UserService:
    Родительский класс: **BaseService**  

[<- на начало](#содержание)

---
## Products:
- ### Модели Products:
  Файл: [models.py](app/products/models.py)
  - #### Product:
      Модель товаров:
    - id: int - PK
    - name: str - название
    - price: int - цена
    - created_at: datetime - дата создания
    - updated_at: datetime - дата обновления
    - is_active: boll - активное/не активное
- ### Маршруты Products:
  Файл: [routers.py](app/products/routers.py)
  - http://127.0.0.1:8000/products
  **(GET)** Просмотр всех продуктов
  - http://127.0.0.1:8000/products
  **(POST)** Добавление продукта
  - http://127.0.0.1:8000/products/{id}
  **(GET)** Получение продукта по ID
  - http://127.0.0.1:8000/products/{id}
  **(PUT)** Обновление продукта по ID
  - http://127.0.0.1:8000/products/{id}
  **(DELETE)** Удаление продукта по ID
- ### Схемы Products:
  Файл: [schemas.py](app/products/schemas.py)
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
- ### Сервис Products:
  Файл: [service.py](app/products/service.py)
  - #### ProductService:
    Родительский класс: **BaseService**  
    Сервис работы с пользователями в БД

[<- на начало](#содержание)

---
