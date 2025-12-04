from typing import Optional, TypeVar

from sqlalchemy import Integer, cast, insert, select

from app.database import async_session_maker


class BaseService:
    """Базовый сервис запросов к БД"""

    model = None

    @classmethod
    async def add(cls, **data) -> None:
        """Создание нового объекта в БД"""
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def find_by_id(cls, model_id: int):
        """Получение объекта по ID"""
        async with async_session_maker() as session:
            query = select(cls.model).filter(cast(cls.model.id, Integer) == model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def update(cls, model_id: int, obj):
        """Изменение объекта по ID"""
        async with async_session_maker() as session:
            pass

    @classmethod
    async def delete(cls, model_id: int) -> bool:
        """Удаление объекта по ID"""
        async with async_session_maker() as session:
            pass

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        """Получение одного объекта"""
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        """Получение всех объектов"""
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()
