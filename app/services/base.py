from typing import Optional, TypeVar

from sqlalchemy import select

from app.database import async_session_maker

T = TypeVar('T')

class BaseService:
    """Базовый сервис запросов к БД"""

    model = None

    @classmethod
    async def add(cls, **data) -> T:
        """Создание нового объекта"""
        async with async_session_maker() as session:
            obj = cls.model(**data)
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return obj

    @classmethod
    async def find_by_id(cls, model_id: int) -> Optional[T]:
        """Получение объекта по ID"""
        async with async_session_maker() as session:
            obj = await session.get(cls.model, model_id)
            return obj

    @classmethod
    async def update(cls, model_id: int, **data: dict) -> Optional[T]:
        """Изменение объекта по ID"""
        async with async_session_maker() as session:
            obj = await session.get(cls.model, model_id)
            if obj:
                for key, value in data.items():
                    setattr(obj, key, value)
                await session.commit()
                await session.refresh(obj)
            return obj

    @classmethod
    async def delete(cls, model_id: int) -> bool:
        """Удаление объекта по ID"""
        async with async_session_maker() as session:
            obj = await session.get(cls.model, model_id)
            if not obj:
                return False
            session.delete(obj)
            await session.commit()
            return True

    @classmethod
    async def find_one_or_none(cls, **filter_by) -> Optional[T]:
        """Получение одного объекта"""
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by) -> list[T]:
        """Получение всех объектов"""
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()
