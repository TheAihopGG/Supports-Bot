from sqlalchemy.orm import mapped_column, Mapped

from .base import Base
from .mixins import IDMixin


class User(Base, IDMixin):
    __tablename__ = "users"

    guild_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    discord_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    is_verified: Mapped[bool] = mapped_column(default=False)


__all__ = ("User",)
