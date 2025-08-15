from disnake import ButtonStyle, MessageInteraction
from disnake.ui import View, button, Button

from .modals import GetSupportFeedbackText


class SendSupportFeedbackView(View):
    def __init__(
        self,
        *,
        support_id: int,
        author_id: int,
    ):
        super().__init__(timeout=None)
        self.support_id = support_id
        self.author_id = author_id

    @button(style=ButtonStyle.secondary, label="Оставить отзыв на саппорта")
    async def send_support_feedback_callback(
        self,
        button: Button,
        inter: MessageInteraction,
    ) -> None:
        await inter.response.send_modal(modal=GetSupportFeedbackText(support_id=self.support_id, author_id=self.author_id))
