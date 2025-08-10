from ...core.base_embeds import SuccessEmbed


class GenderRoleWasSetEmbed(SuccessEmbed):
    def __init__(self) -> None:
        super().__init__(description="Гендер роль успешно установлена.")


class SupportRoleWasSetEmbed(SuccessEmbed):
    def __init__(self) -> None:
        super().__init__(description="Роль поддержки сервера успешно установлена.")


class GuildSetupWasSuccessfulEmbed(SuccessEmbed):
    def __init__(self) -> None:
        super().__init__(description="Сервер успешно настроен.")
        self.add_field(
            "Дополнительная настройка",
            "</set support_role:1403720935605014591> устанавливает роль поддержки сервера.\n"
            "</set female_role:1403720935605014591> устанавливает роль для женского пола.\n"
            "</set male_role:1403720935605014591> устанавливает роль для мужского пола.",
        )


class GuildWasAlreadySetup(SuccessEmbed):
    def __init__(self) -> None:
        super().__init__(description="Сервер уже настроен.")
