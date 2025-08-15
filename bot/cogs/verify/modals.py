from disnake import TextInputStyle, ModalInteraction
from disnake.ui import Modal, TextInput

from ...core.database import session_factory
from ...services.supports_feedbacks import send_support_feedback
from ...services.guilds_settings import get_guild_settings
from .embeds import SupportFeedbackHasSentEmbed


class GetSupportFeedbackText(Modal):
    def __init__(
        self,
        *,
        support_id: int,
        author_id: int,
    ):
        super().__init__(
            title="Отзыв",
            custom_id="get_support_feedback_text",
            components=[
                TextInput(
                    label="Текст",
                    style=TextInputStyle.paragraph,
                    custom_id="support_feedback_text",
                ),
            ],
        )
        self.support_id = support_id
        self.author_id = author_id

    async def callback(self, inter: ModalInteraction) -> None:
        support_feedback_text = inter.text_values["support_feedback_text"]
        async with session_factory() as session:
            if guild_settings := await get_guild_settings(session, inter.guild_id):
                await send_support_feedback(
                    session,
                    guild=inter.guild,
                    guild_settings=guild_settings,
                    author_discord_id=self.author_id,
                    support_discord_id=self.support_id,
                    text=support_feedback_text,
                )
                await inter.author.send(embed=SupportFeedbackHasSentEmbed(support_id=self.support_id, text=support_feedback_text))
