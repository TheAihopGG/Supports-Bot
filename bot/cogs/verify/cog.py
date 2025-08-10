from disnake.ext import commands
from disnake.ext.commands import Param
from disnake import AppCmdInter, Member, Role
from enum import StrEnum, auto

from ...core.database import session_factory
from ...core.embeds import GuildWasNotSetupEmbed, NotEnoughPermissionsEmbed
from ...core.models import User
from ...services.guilds_settings import get_guild_settings
from ...services.users import get_or_create_user_by_discord_id
from .embeds import SupportRoleWasDeletedEmbed, SupportRoleWasNotSetEmbed, IncorrectGenderNameEmbed, YouSuccessfullyVerifiedMemberEmbed, YouSuccessfullyVerifiedEmbed, MemberWasAlreadyVerifiedEmbed


class GenderEnum(StrEnum):
    MALE = auto()
    FEMALE = auto()


class VerifyCog(commands.Cog):
    @commands.slash_command(name="verify", description="Верифицирует участника.")
    async def verify_member(
        self,
        inter: AppCmdInter,
        member: Member = Param(description="Верифицируемый участник."),
        gender_name: GenderEnum = Param(description="Гендер роль."),
    ) -> None:
        async def verify_member_if_not_verified_yet(user: User):
            if not user.is_verified:
                if gender_role := inter.guild.get_role(
                    {
                        GenderEnum.MALE: guild_settings.male_role_id,
                        GenderEnum.FEMALE: guild_settings.female_role_id,
                    }[gender_name]
                ):
                    user.is_verified = True
                    await session.commit()
                    await member.add_roles(gender_role)
                    await member.send(embed=YouSuccessfullyVerifiedEmbed())
                    await inter.response.send_message(embed=YouSuccessfullyVerifiedMemberEmbed())
                else:
                    await inter.response.send_message(embed=IncorrectGenderNameEmbed(), ephemeral=True)
            else:
                await inter.response.send_message(embed=MemberWasAlreadyVerifiedEmbed(), ephemeral=True)

        async with session_factory() as session:
            if inter.author.guild_permissions.administrator:
                if guild_settings := await get_guild_settings(session, guild_id=inter.guild_id):
                    await verify_member_if_not_verified_yet(
                        await get_or_create_user_by_discord_id(
                            session,
                            discord_id=member.id,
                            guild_id=inter.guild_id,
                        )
                    )
                else:
                    await inter.response.send_message(embed=GuildWasNotSetupEmbed(), ephemeral=True)
            else:
                if guild_settings := await get_guild_settings(session, guild_id=inter.guild_id):
                    if guild_settings.support_role_id:
                        if support_role := guild_settings.support_role_id:
                            # if author is in support staff
                            if support_role in inter.author.roles:
                                await verify_member_if_not_verified_yet(
                                    await get_or_create_user_by_discord_id(
                                        session,
                                        discord_id=member.id,
                                        guild_id=inter.guild_id,
                                    )
                                )
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
