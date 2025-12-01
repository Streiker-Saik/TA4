from typing import Optional

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresSettings(BaseSettings):
    """
    Класс для настройки подключения к базе данных Postgres.
    """

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    DATABASE_URL: Optional[str] = None

    @model_validator(mode="before")
    def build_database_url(cls, values) -> dict:
        """Генерирует URL-адрес асинхронного подключения к базе данных Postgres."""

        values["DATABASE_URL"] = (
            f"postgresql+asyncpg://{values['POSTGRES_USER']}:{values['POSTGRES_PASSWORD']}@"
            f"{values['POSTGRES_HOST']}:{values['POSTGRES_PORT']}/{values['POSTGRES_DB']}"
        )
        return values

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = PostgresSettings()
print(settings)