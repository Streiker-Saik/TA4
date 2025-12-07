from datetime import datetime, timezone

from fastapi import Request, Depends
import jwt

from app.config import settings
from app.exceptions import TokenExpireException, TokenAbsentException, IncorrectTokenException, \
    UserIsNonePresentException, UserNotIsAdminException
from app.users.models import User
from app.users.services import UserService


def get_token(request: Request):
    """Получение токена"""
    token = request.cookies.get("ta4_access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    """Проверка авторизованного пользователя"""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except jwt.PyJWTError:
        raise IncorrectTokenException
    expire: str = payload.get("exp")
    if not expire or int(expire) < datetime.now(timezone.utc).timestamp():
        raise TokenExpireException
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsNonePresentException
    user = await UserService.find_by_id(int(user_id))
    if not user:
        raise UserIsNonePresentException
    return user


async def get_current_user_is_admin(current_user: User = Depends(get_current_user)):
    """Проверка пользователя с правами администратора"""
    if not current_user.is_admin:
        raise UserNotIsAdminException
    return current_user
