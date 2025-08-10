from disnake.ext import commands
from disnake import AppCmdInter, Member, Role

from ...core.database import session_factory
from ...core.embeds import NotEnoughPermissionsEmbed, GuildWasNotSetupEmbed
from .embeds import GenderRoleWasSetEmbed, SupportRoleWasSetEmbed, GuildSetupWasSuccessful, GuildWasAlreadySetup
from ...services.guilds_settings import initialize_guild_settings, get_guild_settings
from ...services.users import get_or_create_user_by_discord_id, remove_user_by_discord_id


class GuildSettingsCog(commands.Cog):
    @commands.slash_command()
    async def setup(self, inter: AppCmdInter) -> None:
        if inter.author.guild_permissions.administrator:
            async with session_factory() as session:
                if await initialize_guild_settings(session, guild_id=inter.guild_id):
                    await inter.response.send_message(embed=GuildSetupWasSuccessful())
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
                    await session.commit()
                    await inter.response.send_message(embed=GenderRoleWasSetEmbed())
                else:
                    await inter.response.send_message(embed=GuildWasNotSetupEmbed(), ephemeral=True)
        else:
            await inter.response.send_message(embed=NotEnoughPermissionsEmbed(), ephemeral=True)

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
                    await session.commit()
                    await inter.response.send_message(embed=GenderRoleWasSetEmbed())
                else:
                    await inter.response.send_message(embed=GuildWasNotSetupEmbed(), ephemeral=True)
        else:
            await inter.response.send_message(embed=NotEnoughPermissionsEmbed(), ephemeral=True)

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
                    await session.commit()
                    await inter.response.send_message(embed=SupportRoleWasSetEmbed())
                else:
                    await inter.response.send_message(embed=GuildWasNotSetupEmbed(), ephemeral=True)
        else:
            await inter.response.send_message(embed=NotEnoughPermissionsEmbed(), ephemeral=True)

    @commands.Cog.listener()
    async def on_member_join(self, member: Member) -> None:
        async with session_factory() as session:
            await get_or_create_user_by_discord_id(session, discord_id=member.id, guild_id=member.guild.id)


__all__ = ("GuildSettingsCog",)
