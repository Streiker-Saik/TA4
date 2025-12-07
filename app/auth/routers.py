from fastapi import APIRouter, Response

from app.auth.auth import authenticate_user, create_access_token, get_password_hash
from app.auth.schemas import SUserLogin, SUserRegister
from app.exceptions import UserAlreadyExistsException, IncorrectEmailOrPhoneOrPasswordException
from app.users.services import UserService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
async def register_user(user_data: SUserRegister) -> dict:
    """Регистрация пользователя"""

    existing_email = await UserService.find_one_or_none(email=user_data.email)
    existing_phone = await UserService.find_one_or_none(phone=user_data.phone)

    if existing_email or existing_phone:
        raise UserAlreadyExistsException

    hashed_password = get_password_hash(user_data.password)
    await UserService.add(
        full_name=user_data.full_name, email=user_data.email, phone=user_data.phone, password=hashed_password
    )

    return {"detail": "Пользователь зарегистрирован успешно"}


@router.post("/login")
async def login_user(response: Response, user_data: SUserLogin):
    """Авторизация пользователя"""

    user = await authenticate_user(user_data.email, user_data.phone, user_data.password)
    if not user:
        raise IncorrectEmailOrPhoneOrPasswordException

    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("ta4_access_token", access_token, httponly=True)

    return {"ta4_access_token": access_token}


@router.post("/logout")
async def logout_use(response: Response):
    """Выход пользователя"""
    response.delete_cookie("ta4_access_token")
