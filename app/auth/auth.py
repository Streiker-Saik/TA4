from datetime import datetime, timedelta, timezone

import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from app.config import settings
from app.users.services import UserService

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


def get_password_hash(password: str) -> str:
    """Получение хэшированного пароля"""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Проверка пароля"""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    """Создание токена"""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoder_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return encoder_jwt


async def authenticate_user(email: EmailStr = None, phone: str = None, password: str = None):
    """Аутентификация пользователя"""
    if email:
        user = await UserService.find_one_or_none(email=email)
    else:
        user = await UserService.find_one_or_none(phone=phone)

    if not user or not verify_password(plain_password=password, hashed_password=user.password):
        return None
    return user
