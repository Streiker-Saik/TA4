from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SProductCreate(BaseModel):
    """Схема для создания продукта
    Attributes:
        name: Название
        price: Цена
    """

    name: str
    price: int


class SProductResponse(BaseModel):
    """Схема получение информации о продукте
    Attributes:
        id: id продукта
        name: Название
        price: Цена
        create_at: Дата и время создания
        updated_at: Дата и время изменения
        is_active: Активное/не активное
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: int
    name: str
    price: int
    create_at: datetime
    updated_at: datetime
    is_active: bool


class SProductUpdate(BaseModel):
    """Схема изменения информации о продукте
    Attributes:
        name: Название
        price: Цена
        is_active: Активное/не активное
    """

    name: str
    price: int
    is_active: bool
