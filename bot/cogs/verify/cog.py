from disnake.ext import commands
from disnake import AppCmdInter, Member, Role

from ...core.database import session_factory
from ...core.models import GuildSettings
from ...services.guilds_settings import get_guild_settings


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
                if support_role := await inter.guild.get_role(guild_settings.support_role_id):
                    # if author is in support staff
                    if support_role in inter.author.roles:
                        # if gender_role is valid
                        if gender_role in {guild_settings.male_role_id, guild_settings.female_role_id}:
                            await member.add_roles(gender_role)
                            await member.send(content="Вы успешно верифицированы")
                            await inter.response.send_message(content="Вы успешно верифицировали участника")
                        else:
                            await inter.response.send_message(content="Некорректная роль", ephemeral=True)
                    else:
                        await inter.response.send_message(content="Вы не состоите в составе поддержки сервера", ephemeral=True)
                else:
                    await inter.response.send_message(content="Роль поддержки сервера, вероятна была удалена", ephemeral=True)
            else:
                await inter.response.send_message(content="Сервер не настроен", ephemeral=True)


__all__ = ("VerifyCog",)
