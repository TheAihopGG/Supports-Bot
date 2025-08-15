from disnake import Member
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


class YouSuccessfullyVerifiedEmbed(SuccessEmbed):
    def __init__(self, support: Member) -> None:
        super().__init__(description="Вы успешно верифицированы.")
        self.add_field("Вас верифицировал", support.mention)
        self.set_footer(text="Нажмите кнопку ниже чтобы оставить отзыв на саппорта.")


class MemberWasAlreadyVerifiedEmbed(ErrorEmbed):
    def __init__(self) -> None:
        super().__init__(description="Участник уже верифицирован.")


class GenderRolesWasNotSetEmbed(ErrorEmbed):
    def __init__(self) -> None:
        super().__init__(description="Роли гендера не установлены или удалены")


class SupportFeedbackHasSentEmbed(SuccessEmbed):
    def __init__(
        self,
        *,
        support_id: int,
        text: str,
    ):
        super().__init__(description="Вы успешно отправили отзыв")
        self.add_field("Текст отзыва", text)
        self.add_field("Саппорт", f"<@{support_id}>")
