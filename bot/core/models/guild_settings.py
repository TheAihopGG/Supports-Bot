from sqlalchemy.orm import mapped_column, Mapped

from .base import Base
from .mixins import IDMixin


class GuildSettings(Base, IDMixin):
    __tablename__ = "guilds_settings"
    guild_id: Mapped[int] = mapped_column(unique=True, nullable=False)

    male_role_id: Mapped[int] = mapped_column(nullable=True)
    female_role_id: Mapped[int] = mapped_column(nullable=True)
    support_role_id: Mapped[int] = mapped_column(nullable=True)


__all__ = ("GuildSettings",)
