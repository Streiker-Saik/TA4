import re

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, model_validator


class SUserRegister(BaseModel):
    """Схема для регистрации пользователя с валидацией данных
    Attributes:
        full_name: ФИО пользователя
        email: Адрес электронной почты
        phone: Номер телефона, должен начинаться на +7 и содержать 10 цифр
        password: Пароль, должен соответствовать:
            не менее 8 символов;
            только латинские буквы;
            минимум 1 заглавная буква;
            минимум 1 строчные буква;
            минимум 1 спец символы ($%&!:)
        confirm_password: Подтверждение пароля
    """

    full_name: str
    email: EmailStr
    phone: str
    password: str
    confirm_password: str

    @model_validator(mode="before")
    # @classmethod
    def check_phone_match(cls, values: dict) -> dict:
        """Проверяем, что номер соответствует формату +7XXXXXXXXXX"""
        phone = values.get("phone")

        if phone is None:
            raise HTTPException(status_code=400, detail="Номер телефона не может быть пустым.")

        pattern = re.compile(r"^\+7\d{10}$")
        if not pattern.match(phone):
            raise HTTPException(status_code=400, detail="Номер телефона должен начинаться на +7 и содержать 10 цифр")
        return values

    @model_validator(mode="before")
    # @classmethod
    def check_password_match(cls, values: dict) -> dict:
        """Проверяем, что пароль соответствует требованиям"""
        password = values.get("password")
        confirm_password = values.get("confirm_password")

        if password is None or confirm_password is None:
            raise HTTPException(status_code=400, detail="Пароль и подтверждение пароля не могут быть пустыми.")

        pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[$%&!:])[A-Za-z$%&!:]{8,}$")
        if not pattern.match(password):
            raise HTTPException(
                status_code=400,
                detail="Пароль должен содержать:\n"
                "- не менее 8 символов,\n"
                "- только латинские буквы,\n"
                "- хотя бы одну заглавную букву,\n"
                "- хотя бы одну строчную букву,\n"
                "- хотя бы один спец. символ ($%&!:)",
            )

        if password != confirm_password:
            raise HTTPException(status_code=400, detail="Пароли не совпадает")
        return values


class SUserLogin(BaseModel):
    """Схема для авторизации пользователя
    Attributes:
        email: Адрес электронной почты
        phone: Номер телефона
        password: Пароль.
    """

    email: EmailStr
    phone: str
    password: str
