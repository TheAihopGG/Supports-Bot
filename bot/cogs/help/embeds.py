from ...core.base_embeds import InfoEmbed
from ...core.enums import CommandsIdEnum
from .enums import HelpMenuSectionsEnum


class HelpForSectionEmbed(InfoEmbed):
    def __init__(self, section_name: HelpMenuSectionsEnum):
        super().__init__()
        match section_name:
            case HelpMenuSectionsEnum.GUILD_SETTINGS:
                self.add_field(
                    f"Команды раздела **{section_name}**",
                    f"</set support_role:{CommandsIdEnum.SET_CMD_ID}> устанавливает роль поддержки сервера.\n"
                    f"</set female_role:{CommandsIdEnum.SET_CMD_ID}> устанавливает роль для женского пола.\n"
                    f"</set unverified_role:{CommandsIdEnum.SET_CMD_ID}> устанавливает роль для женского пола.\n"
                    f"</set male_role:{CommandsIdEnum.SET_CMD_ID}> устанавливает роль для мужского пола.\n"
                    f"</setup:{CommandsIdEnum.SETUP_CMD_ID}> устанавливает роль для женского пола.\n",
                )
            case HelpMenuSectionsEnum.VERIFICATION:
                self.add_field(
                    f"Команды раздела **{section_name}**", f"</verify:{CommandsIdEnum.VERIFY_CMD_ID}> верифицирует участника, выдаёт ему гендер-роль и забирает роль не верифицированного участника."
                )
            case HelpMenuSectionsEnum.COMMON:
                self.add_field(f"Команды раздела **{section_name}**", f"</help:{CommandsIdEnum.HELP_CMD_ID}> помощь по функционалу бота.")


class HelpEmbed(InfoEmbed):
    def __init__(self) -> None:
        super().__init__(description="Выберите раздел, по которому вы хотите получить помощь.")
