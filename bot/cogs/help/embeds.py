from ...core.base_embeds import InfoEmbed
from .enums import HelpMenuSectionsEnum


class HelpForSectionEmbed(InfoEmbed):
    def __init__(self, section_name: HelpMenuSectionsEnum):
        super().__init__()
        match section_name:
            case HelpMenuSectionsEnum.GUILD_SETTINGS:
                self.add_field(
                    f"Команды раздела **{section_name}**",
                    "</set support_role:1403720935605014591> устанавливает роль поддержки сервера.\n"
                    "</set female_role:1403720935605014591> устанавливает роль для женского пола.\n"
                    "</set male_role:1403720935605014591> устанавливает роль для мужского пола.",
                )
            case HelpMenuSectionsEnum.VERIFICATION:
                self.add_field(f"Команды раздела **{section_name}**", "</verify:1403720935605014592> устанавливает роль поддержки сервера.")


class HelpEmbed(InfoEmbed):
    def __init__(self) -> None:
        super().__init__(description="Выберите раздел, по которому вы хотите получить помощь.")
