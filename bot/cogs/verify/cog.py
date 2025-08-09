from disnake.ext import commands
from disnake import AppCmdInter, Member, Role

from ...core.database import session_factory
from ...services.guilds_settings import get_guild_settings
from ...services.user import get_or_create_user_by_discord_id


class VerifyCog(commands.Cog):
    @commands.slash_command()
    async def verify(
        self,
        inter: AppCmdInter,
        member: Member,
        gender_role: Role,
    ) -> None:
        async with session_factory() as session:
            if guild_settings := await get_guild_settings(session, guild_id=inter.guild_id):
                if support_role := inter.guild.get_role(guild_settings.support_role_id):
                    # if author is in support staff
                    if support_role in inter.author.roles:
                        user = await get_or_create_user_by_discord_id(session, discord_id=member.id)
                        if not user.is_verified:
                            # if gender_role is valid
                            if gender_role.id in {guild_settings.male_role_id, guild_settings.female_role_id}:
                                user.is_verified = True
                                await session.commit()
                                await member.add_roles(gender_role)
                                await member.send(content="Вы успешно верифицированы")
                                await inter.response.send_message(content="Вы успешно верифицировали участника")
                            else:
                                await inter.response.send_message(content="Некорректная роль", ephemeral=True)
                        else:
                            await inter.response.send_message(content="Участник уже верифицирован", ephemeral=True)
                    else:
                        await inter.response.send_message(content="Вы не состоите в составе поддержки сервера", ephemeral=True)
                else:
                    await inter.response.send_message(content="Роль поддержки сервера, вероятна была удалена", ephemeral=True)
            else:
                await inter.response.send_message(content="Сервер не настроен", ephemeral=True)


__all__ = ("VerifyCog",)
