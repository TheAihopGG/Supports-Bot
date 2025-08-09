from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column


class IDMixin:
    @declared_attr
    def id(cls) -> Mapped[int]:
        return mapped_column(primary_key=True, index=True)


class GuildIDMixin:

    @declared_attr
    def guild_id(cls) -> Mapped[int]:
        return mapped_column(unique=True, nullable=False)


__all__ = ("IDMixin",)
