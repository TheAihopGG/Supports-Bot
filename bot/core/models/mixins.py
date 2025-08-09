from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column


class IDMixin:
    @declared_attr
    def id(cls) -> Mapped[int]:
        return mapped_column(primary_key=True, index=True)


class GuildIDMixin:
    _is_guild_id_foreign_key = False

    @declared_attr
    def guild_id(cls) -> Mapped[int]:
        return mapped_column(unique=True, nullable=False) if cls._is_guild_id_foreign_key else mapped_column(ForeignKey("guilds_settings.guild_id"), nullable=False)


__all__ = ("IDMixin",)
