from sqlalchemy.orm import mapped_column, Mapped

from .base import Base
from .mixins import IDMixin, GuildIDMixin


class User(
    Base,
    IDMixin,
    GuildIDMixin,
):
    __tablename__ = "users"
    _is_guild_id_foreign_key = True

    discord_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    is_verified: Mapped[bool] = mapped_column(default=False)


__all__ = ("User",)
