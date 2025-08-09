from disnake.ext import commands
from disnake import AppCmdInter

from ...core.database import session_factory
from ...core.models import GuildSettings
from ...services.guilds_settings import initialize_guild_settings


class CommonCog(commands.Cog):
    @commands.slash_command()
    async def setup(self, inter: AppCmdInter) -> None:
        if inter.author.guild_permissions.administrator:
            async with session_factory() as session:
                if await initialize_guild_settings(session, guild_id=inter.guild_id):
                    await inter.response.send_message(content="Успешно")
                else:
                    await inter.response.send_message(content="Сервер уже настроен")
        else:
            await inter.response.send_message(content="Недостаточно прав")


__all__ = ("CommonCog",)
