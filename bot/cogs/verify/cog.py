from disnake.ext import commands
from disnake.ext.commands import Param
from disnake import AppCmdInter, Member
from disnake.ext.commands.errors import CommandInvokeError
from enum import StrEnum, auto
from sqlalchemy.ext.asyncio import AsyncSession

from ...core.database import session_factory
from ...core.embeds import GuildWasNotSetupEmbed, NotEnoughPermissionsEmbed
from ...core.models import User
from ...services.guilds_settings import get_guild_settings
from ...services.users import get_or_create_user_by_discord_id
from .embeds import (
    SupportRoleWasDeletedEmbed,
    SupportRoleWasNotSetEmbed,
    GenderRolesWasNotSetEmbed,
    YouSuccessfullyVerifiedMemberEmbed,
    YouSuccessfullyVerifiedEmbed,
    MemberWasAlreadyVerifiedEmbed,
    IncorrectGenderNameEmbed,
)


class GenderEnum(StrEnum):
    male = auto()
    female = auto()


class VerifyCog(commands.Cog):
    @commands.slash_command(name="verify", description="Верифицирует участника.")
    async def verify_member(
        self,
        inter: AppCmdInter,
        member: Member = Param(description="Верифицируемый участник."),
        gender_name: GenderEnum = Param(description="Гендер роль."),
    ) -> None:
        async with session_factory() as session:
            if inter.author.guild_permissions.administrator:
                if guild_settings := await get_guild_settings(session, guild_id=inter.guild_id):
                    user = await get_or_create_user_by_discord_id(
                        session,
                        discord_id=member.id,
                        guild_id=inter.guild_id,
                    )
                    if not user.is_verified:
                        if gender_role_id := {
                            GenderEnum.male: guild_settings.male_role_id,
                            GenderEnum.female: guild_settings.female_role_id,
                        }.get(gender_name, None):
                            if gender_role := inter.guild.get_role(gender_role_id):
                                user.is_verified = True
                                # remove unverified role
                                if unverified_role := member.guild.get_role(guild_settings.unverified_role_id):
                                    await member.remove_roles(unverified_role)
                                await member.add_roles(gender_role)
                                await session.commit()
                                try:
                                    await member.send(embed=YouSuccessfullyVerifiedEmbed())
                                except CommandInvokeError:
                                    pass
                                await inter.response.send_message(embed=YouSuccessfullyVerifiedMemberEmbed())
                            else:
                                await inter.response.send_message(embed=GenderRolesWasNotSetEmbed(), ephemeral=True)
                        else:
                            await inter.response.send_message(embed=IncorrectGenderNameEmbed(), ephemeral=True)
                    else:
                        await inter.response.send_message(embed=MemberWasAlreadyVerifiedEmbed(), ephemeral=True)
                else:
                    await inter.response.send_message(embed=GuildWasNotSetupEmbed(), ephemeral=True)
            else:
                if guild_settings := await get_guild_settings(session, guild_id=inter.guild_id):
                    if guild_settings.support_role_id:
                        if support_role := guild_settings.support_role_id:
                            # if author is in support staff
                            if support_role in inter.author.roles:
                                user = await get_or_create_user_by_discord_id(
                                    session,
                                    discord_id=member.id,
                                    guild_id=inter.guild_id,
                                )
                                if not user.is_verified:
                                    if gender_role_id := {
                                        GenderEnum.male: guild_settings.male_role_id,
                                        GenderEnum.female: guild_settings.female_role_id,
                                    }.get(gender_name, None):
                                        if gender_role := inter.guild.get_role(gender_role_id):
                                            user.is_verified = True
                                            # remove unverified role
                                            if unverified_role := member.guild.get_role(guild_settings.unverified_role_id):
                                                await member.remove_roles(unverified_role)
                                            await member.add_roles(gender_role)
                                            await session.commit()
                                            try:
                                                await member.send(embed=YouSuccessfullyVerifiedEmbed())
                                            except CommandInvokeError:
                                                pass
                                            await inter.response.send_message(embed=YouSuccessfullyVerifiedMemberEmbed())
                                        else:
                                            await inter.response.send_message(embed=GenderRolesWasNotSetEmbed(), ephemeral=True)
                                    else:
                                        await inter.response.send_message(embed=IncorrectGenderNameEmbed(), ephemeral=True)
                                else:
                                    await inter.response.send_message(embed=MemberWasAlreadyVerifiedEmbed(), ephemeral=True)
                            else:
                                await inter.response.send_message(content=NotEnoughPermissionsEmbed(), ephemeral=True)
                        else:
                            await inter.response.send_message(embed=SupportRoleWasDeletedEmbed(), ephemeral=True)
                    else:
                        await inter.response.send_message(
                            embed=SupportRoleWasNotSetEmbed(),
                            ephemeral=True,
                        )
                else:
                    await inter.response.send_message(embed=GuildWasNotSetupEmbed(), ephemeral=True)


__all__ = ("VerifyCog",)
