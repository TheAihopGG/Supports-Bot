from .base_embeds import ErrorEmbed


class GuildWasNotSetupEmbed(ErrorEmbed):
    def __init__(self):
        super().__init__(description="Сервер не настроен. Используйте команду </setup:1403720935605014590>, чтобы настроить сервер.")


class NotEnoughPermissionsEmbed(ErrorEmbed):
    def __init__(self):
        super().__init__(description="Недостаточно прав.")
