from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ...core.models import GuildSettings


async def get_guild_settings(session: AsyncSession, *, guild_id: int) -> GuildSettings | None:
    return (
        await session.execute(
            select(GuildSettings).where(GuildSettings.guild_id == guild_id),
        )
    ).scalar_one_or_none()


async def initialize_guild_settings(session: AsyncSession, *, guild_id: int) -> bool:
    # check is guild settings exists
    if not await get_guild_settings(session, guild_id=guild_id):
        session.add(GuildSettings(guild_id=guild_id))
        await session.commit()
        return True
    else:
        return False


__all__ = ("get_guild_settings", "initialize_guild_settings")
