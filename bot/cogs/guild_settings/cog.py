from disnake.ext import commands
from disnake import AppCmdInter, Role

from ...core.database import session_factory
from ...services.guilds_settings import initialize_guild_settings, get_guild_settings


class GuildSettingsCog(commands.Cog):
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

    @commands.slash_command()
    async def set(
        self,
        inter: AppCmdInter,
    ) -> None:
        pass

    @set.sub_command()
    async def female_role(
        self,
        inter: AppCmdInter,
        role: Role,
    ) -> None:
        if inter.author.guild_permissions.administrator:
            async with session_factory() as session:
                if guild_settings := await get_guild_settings(session, guild_id=inter.guild_id):
                    guild_settings.female_role_id = role.id
                    await session.refresh(guild_settings)
                    await session.commit()
                    await inter.response.send_message(content="Успешно")
                else:
                    await inter.response.send_message(content="Сервер уже настроен")
        else:
            await inter.response.send_message(content="Недостаточно прав")

    @set.sub_command()
    async def male_role(
        self,
        inter: AppCmdInter,
        role: Role,
    ) -> None:
        if inter.author.guild_permissions.administrator:
            async with session_factory() as session:
                if guild_settings := await get_guild_settings(session, guild_id=inter.guild_id):
                    guild_settings.male_role_id = role.id
                    await session.refresh(guild_settings)
                    await session.commit()
                    await inter.response.send_message(content="Успешно")
                else:
                    await inter.response.send_message(content="Сервер уже настроен")
        else:
            await inter.response.send_message(content="Недостаточно прав")

    @set.sub_command()
    async def support_role(
        self,
        inter: AppCmdInter,
        role: Role,
    ) -> None:
        if inter.author.guild_permissions.administrator:
            async with session_factory() as session:
                if guild_settings := await get_guild_settings(session, guild_id=inter.guild_id):
                    guild_settings.support_role_id = role.id
                    await session.refresh(guild_settings)
                    await session.commit()
                    await inter.response.send_message(content="Успешно")
                else:
                    await inter.response.send_message(content="Сервер уже настроен")
        else:
            await inter.response.send_message(content="Недостаточно прав")


__all__ = ("GuildSettingsCog",)
