from disnake import MessageInteraction, SelectOption
from disnake.ui import Select, View

from .enums import HelpMenuSectionsEnum
from .embeds import HelpForSectionEmbed


class HelpView(View):
    class HelpMenuSelect(Select):
        def __init__(self) -> None:
            super().__init__(
                placeholder="Выберите раздел помощи",
                min_values=1,
                max_values=1,
                options=[
                    SelectOption(label="Настройка сервера", value=HelpMenuSectionsEnum.GUILD_SETTINGS),
                    SelectOption(label="Верификация", value=HelpMenuSectionsEnum.VERIFICATION),
                    SelectOption(label="Общее", value=HelpMenuSectionsEnum.COMMON),
                ],
            )

        async def callback(self, inter: MessageInteraction):
            section_name: HelpMenuSectionsEnum = inter.values[0]
            await inter.response.send_message(embed=HelpForSectionEmbed(section_name=section_name), ephemeral=True)

    def __init__(self) -> None:
        super().__init__(timeout=120)
        self.add_item(HelpView.HelpMenuSelect())
