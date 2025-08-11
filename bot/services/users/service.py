from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ...core.models import User


async def get_or_create_user_by_discord_id(session: AsyncSession, *, discord_id: int, guild_id: int) -> User:
    if user := (
        await session.execute(
            select(User).where(User.discord_id == discord_id),
        )
    ).scalar_one_or_none():
        return user
    else:
        user = User(discord_id=discord_id, guild_id=guild_id)
        session.add(user)
        return user


__all__ = ("get_or_create_user_by_discord_id",)
