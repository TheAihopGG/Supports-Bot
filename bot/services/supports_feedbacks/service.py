import re
from disnake import Guild
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ...core.models import SupportFeedback, GuildSettings
from .embeds import SupportFeedbackEmbed


async def create_support_feedback(
    session: AsyncSession,
    *,
    guild_id: int,
    author_discord_id: int,
    support_discord_id: int,
    text: str,
) -> None:
    if support_feedback := (
        await session.execute(
            select(SupportFeedback).where(
                SupportFeedback.guild_id == guild_id,
                SupportFeedback.author_discord_id == author_discord_id,
                SupportFeedback.support_discord_id == support_discord_id,
            )
        )
    ).scalar_one_or_none():
        if support_feedback.text != text:
            support_feedback.text = text
            await session.commit()
    else:
        session.add(
            SupportFeedback(
                guild_id=guild_id,
                author_discord_id=author_discord_id,
                support_discord_id=support_discord_id,
                text=text,
            )
        )
        await session.commit()


async def send_support_feedback(
    session: AsyncSession,
    *,
    guild: Guild,
    guild_settings: GuildSettings,
    author_discord_id: int,
    support_discord_id: int,
    text: str,
) -> None:
    if supports_feedback_channel := guild.get_channel(guild_settings.supports_feedbacks_channel_id):
        await supports_feedback_channel.send(
            embed=SupportFeedbackEmbed(
                author_discord_id=author_discord_id,
                support_discord_id=support_discord_id,
                text=text,
            )
        )
        await create_support_feedback(
            session,
            guild_id=guild.id,
            author_discord_id=author_discord_id,
            support_discord_id=support_discord_id,
            text=text,
        )


__all__ = (
    "send_support_feedback",
    "create_support_feedback",
)
