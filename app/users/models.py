from sqlalchemy import Boolean, Column, Integer, String

from app.database import Base


class User(Base):
    """Модель пользователей"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"<User id={self.id} email={self.email} phone={self.phone}>"
