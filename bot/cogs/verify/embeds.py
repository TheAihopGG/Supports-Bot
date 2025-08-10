from ...core.base_embeds import ErrorEmbed, SuccessEmbed


class SupportRoleWasDeletedEmbed(ErrorEmbed):
    def __init__(self) -> None:
        super().__init__(description="Роль поддержки сервера, вероятна была удалена.")


class SupportRoleWasNotSetEmbed(ErrorEmbed):
    def __init__(self) -> None:
        super().__init__(description="Роль поддержки сервера не установлена. Используйте команду </set support_role:1403720935605014591>, чтобы установить роль поддержки сервера.")


class IncorrectGenderNameEmbed(ErrorEmbed):
    def __init__(self) -> None:
        super().__init__(description="Некорректное название гендера.")


class YouSuccessfullyVerifiedMemberEmbed(SuccessEmbed):
    def __init__(self) -> None:
        super().__init__(description="Вы успешно верифицировали участника.")


class YouSuccessfullyVerifiedEmbed(ErrorEmbed):
    def __init__(self) -> None:
        super().__init__(description="Вы успешно верифицированы.")


class MemberWasAlreadyVerifiedEmbed(ErrorEmbed):
    def __init__(self) -> None:
        super().__init__(description="Участник уже верифицирован.")
