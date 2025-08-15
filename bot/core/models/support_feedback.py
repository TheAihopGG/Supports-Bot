from sqlalchemy.orm import mapped_column, Mapped

from .base import Base
from .mixins import IDMixin


class SupportFeedback(Base, IDMixin):
    __tablename__ = "users"

    guild_id: Mapped[int] = mapped_column(nullable=False)
    author_discord_id: Mapped[int] = mapped_column(nullable=False)
    support_discord_id: Mapped[int] = mapped_column(nullable=False)
    text: Mapped[int] = mapped_column(nullable=False)


__all__ = ("SupportFeedback",)
