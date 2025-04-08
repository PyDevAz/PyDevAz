from typing import Any

from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, declared_attr

class Base(DeclarativeBase):
    id: Any

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

class Tasks(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    name: Mapped[str]
    pomodoro_count: Mapped[int]
    category_id: Mapped[int]

class Categories(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    type: Mapped[str]


class User(Base):
    __tablename__ = 'users'

    name: Mapped[str] = mapped_column(primary_key=True)
    password: Mapped[int]
    age: Mapped[int]