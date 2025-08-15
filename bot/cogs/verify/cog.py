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
from .views import SendSupportFeedbackView


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
        await inter.response.defer()
        async with session_factory() as session:
            if guild_settings := await get_guild_settings(session, guild_id=inter.guild_id):
                if guild_settings.support_role_id:
                    if support_role := guild_settings.support_role_id:
                        # if author is in support staff
                        if support_role in inter.author.roles or inter.author.guild_permissions.administrator:
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
                                            await member.send(embed=YouSuccessfullyVerifiedEmbed(), view=SendSupportFeedbackView())
                                        except CommandInvokeError:
                                            pass
                                        await inter.edit_original_response(embed=YouSuccessfullyVerifiedMemberEmbed())
                                    else:
                                        await inter.edit_original_response(embed=GenderRolesWasNotSetEmbed())
                                else:
                                    await inter.edit_original_response(embed=IncorrectGenderNameEmbed())
                            else:
                                await inter.edit_original_response(embed=MemberWasAlreadyVerifiedEmbed())
                        else:
                            await inter.edit_original_response(content=NotEnoughPermissionsEmbed())
                    else:
                        await inter.edit_original_response(embed=SupportRoleWasDeletedEmbed())
                else:
                    await inter.edit_original_response(
                        embed=SupportRoleWasNotSetEmbed(),
                        ephemeral=True,
                    )
            else:
                await inter.edit_original_response(embed=GuildWasNotSetupEmbed())


__all__ = ("VerifyCog",)
