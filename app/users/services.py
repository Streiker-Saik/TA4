from app.services.base import BaseService
from app.users.models import User


class UserService(BaseService):
    """Сервис работы с пользователями в БД"""

    model = User
