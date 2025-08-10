from sqlalchemy.orm import mapped_column, Mapped

from .base import Base
from .mixins import IDMixin, GuildIDMixin


class GuildSettings(Base, IDMixin, GuildIDMixin):
    __tablename__ = "guilds_settings"

    male_role_id: Mapped[int] = mapped_column(nullable=True)
    female_role_id: Mapped[int] = mapped_column(nullable=True)
    support_role_id: Mapped[int] = mapped_column(nullable=True)
    unverified_role_id: Mapped[int] = mapped_column(nullable=True)


__all__ = ("GuildSettings",)
