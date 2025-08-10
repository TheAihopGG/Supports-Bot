from ...core.base_embeds import SuccessEmbed


class GenderRoleWasSetEmbed(SuccessEmbed):
    def __init__(self) -> None:
        super().__init__(description="Гендер роль успешно установлена.")


class SupportRoleWasSetEmbed(SuccessEmbed):
    def __init__(self) -> None:
        super().__init__(description="Роль поддержки сервера успешно установлена.")


class GuildSetupWasSuccessful(SuccessEmbed):
    def __init__(self) -> None:
        super().__init__(description="Сервер успешно настроен.")


class GuildWasAlreadySetup(SuccessEmbed):
    def __init__(self) -> None:
        super().__init__(description="Сервер уже настроен.")
