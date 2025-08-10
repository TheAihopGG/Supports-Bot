from disnake.ext import commands
from disnake.ext.commands import Param
from disnake import AppCmdInter, Member, Role

from ...core.database import session_factory
from ...core.embeds import NotEnoughPermissionsEmbed, GuildWasNotSetupEmbed
from .embeds import GenderRoleWasSetEmbed, SupportRoleWasSetEmbed, GuildSetupWasSuccessfulEmbed, GuildWasAlreadySetup, UnverifiedRoleWasSetEmbed
from ...services.guilds_settings import initialize_guild_settings, get_guild_settings
from ...services.users import get_or_create_user_by_discord_id


class GuildSettingsCog(commands.Cog):
    @commands.slash_command(name="setup", description="Настраивает сервер.")
    async def setup(self, inter: AppCmdInter) -> None:
        if inter.author.guild_permissions.administrator:
            async with session_factory() as session:
                if await initialize_guild_settings(session, guild_id=inter.guild_id):
                    await inter.response.send_message(embed=GuildSetupWasSuccessfulEmbed())
                else:
                    await inter.response.send_message(embed=GuildWasAlreadySetup())
        else:
            await inter.response.send_message(embed=NotEnoughPermissionsEmbed(), ephemeral=True)

    @commands.slash_command()
    async def set(
        self,
        inter: AppCmdInter,
    ) -> None:
        pass

    @set.sub_command(name="female_role", description="Устанавливает роль для женского пола.")
    async def female_role(
        self,
        inter: AppCmdInter,
        role: Role = Param(description="Роль, которая будет установлена как роль для женского пола."),
    ) -> None:
        if inter.author.guild_permissions.administrator:
            async with session_factory() as session:
                if guild_settings := await get_guild_settings(session, guild_id=inter.guild_id):
                    guild_settings.female_role_id = role.id
                    await session.commit()
                    await inter.response.send_message(embed=GenderRoleWasSetEmbed())
                else:
                    await inter.response.send_message(embed=GuildWasNotSetupEmbed(), ephemeral=True)
        else:
            await inter.response.send_message(embed=NotEnoughPermissionsEmbed(), ephemeral=True)

    @set.sub_command(name="male_role", description="Устанавливает роль для мужского пола.")
    async def male_role(
        self,
        inter: AppCmdInter,
        role: Role = Param(description="Роль, которая будет установлена как роль для мужского пола."),
    ) -> None:
        if inter.author.guild_permissions.administrator:
            async with session_factory() as session:
                if guild_settings := await get_guild_settings(session, guild_id=inter.guild_id):
                    guild_settings.male_role_id = role.id
                    await session.commit()
                    await inter.response.send_message(embed=GenderRoleWasSetEmbed())
                else:
                    await inter.response.send_message(embed=GuildWasNotSetupEmbed(), ephemeral=True)
        else:
            await inter.response.send_message(embed=NotEnoughPermissionsEmbed(), ephemeral=True)

    @set.sub_command(name="support_role", description="Устанавливает роль для поддержки сервера.")
    async def support_role(
        self,
        inter: AppCmdInter,
        role: Role = Param(description="Роль, которая будет установлена как роль для поддержки сервера."),
    ) -> None:
        if inter.author.guild_permissions.administrator:
            async with session_factory() as session:
                if guild_settings := await get_guild_settings(session, guild_id=inter.guild_id):
                    guild_settings.support_role_id = role.id
                    await session.commit()
                    await inter.response.send_message(embed=SupportRoleWasSetEmbed())
                else:
                    await inter.response.send_message(embed=GuildWasNotSetupEmbed(), ephemeral=True)
        else:
            await inter.response.send_message(embed=NotEnoughPermissionsEmbed(), ephemeral=True)

    @set.sub_command(name="unverified_role", description="Устанавливает роль для не верифицированных участников.")
    async def unverified_role(
        self,
        inter: AppCmdInter,
        role: Role = Param(description="Роль, которая будет установлена как роль для не верифицированных участников."),
    ) -> None:
        if inter.author.guild_permissions.administrator:
            async with session_factory() as session:
                if guild_settings := await get_guild_settings(session, guild_id=inter.guild_id):
                    guild_settings.unverified_role_id = role.id
                    await session.commit()
                    await inter.response.send_message(embed=UnverifiedRoleWasSetEmbed())
                else:
                    await inter.response.send_message(embed=GuildWasNotSetupEmbed(), ephemeral=True)
        else:
            await inter.response.send_message(embed=NotEnoughPermissionsEmbed(), ephemeral=True)

    @commands.Cog.listener()
    async def on_member_join(self, member: Member) -> None:
        async with session_factory() as session:
            # add member to database
            await get_or_create_user_by_discord_id(session, discord_id=member.id, guild_id=member.guild.id)


__all__ = ("GuildSettingsCog",)
