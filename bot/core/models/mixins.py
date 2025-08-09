from sqlalchemy.orm import declared_attr, Mapped, mapped_column


class IDMixin:
    @declared_attr
    def id(cls) -> Mapped[int]:
        return mapped_column(primary_key=True, index=True)


__all__ = ("IDMixin",)
