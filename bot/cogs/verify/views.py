from disnake import ButtonStyle, Guild, MessageInteraction
from disnake.ui import View, button, Button

from .modals import GetSupportFeedbackText


class SendSupportFeedbackView(View):
    def __init__(
        self,
        *,
        support_id: int,
        author_id: int,
        guild: Guild,
    ):
        super().__init__(timeout=None)
        self.support_id = support_id
        self.author_id = author_id
        self.guild = guild
        self.clicked = False

    @button(style=ButtonStyle.secondary, label="Оставить отзыв")
    async def send_support_feedback_callback(
        self,
        button: Button,
        inter: MessageInteraction,
    ) -> None:
        if not self.clicked:
            await inter.response.send_modal(
                modal=GetSupportFeedbackText(
                    support_id=self.support_id,
                    author_id=self.author_id,
                    guild=self.guild,
                )
            )
            self.clicked = True
