from fastapi import HTTPException, status

UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Email или телефон уже зарегистрирован"
)

IncorrectEmailOrPhoneOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверная почта или номер телефона или пароль"
)

TokenAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токен отсутствует"
)

IncorrectTokenException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверный формат токена"
)

TokenExpireException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токен истек"
)

UserIsNonePresentException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

UserNotIsAdminException = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="Не достаточно прав"
)

PhoneNoneException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Номер телефона не может быть пустым."
)

IncorrectPhoneException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Номер телефона должен начинаться на +7 и содержать 10 цифр"
)

PasswordNoneException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Пароль и подтверждение пароля не могут быть пустыми."
)

IncorrectPasswordException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Пароль должен содержать:\n"
           "- не менее 8 символов,\n"
           "- только латинские буквы,\n"
           "- хотя бы одну заглавную букву,\n"
           "- хотя бы одну строчную букву,\n"
           "- хотя бы один спец. символ ($%&!:)",
)

PasswordsDontMatchException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Пароли не совпадает"
)