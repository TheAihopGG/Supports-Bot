from disnake import Guild, TextInputStyle, ModalInteraction
from disnake.ui import Modal, TextInput

from ...core.database import session_factory
from ...core.configuration import SUPPORT_FEEDBACK_TEXT_MAX_LENGTH
from ...services.supports_feedbacks import send_support_feedback
from ...services.guilds_settings import get_guild_settings
from .embeds import SupportFeedbackHasSentEmbed


class GetSupportFeedbackText(Modal):
    def __init__(
        self,
        *,
        support_id: int,
        author_id: int,
        guild: Guild,
    ):
        super().__init__(
            title="Отзыв",
            custom_id="get_support_feedback_text",
            components=[
                TextInput(
                    label="Текст",
                    style=TextInputStyle.paragraph,
                    custom_id="support_feedback_text",
                    max_length=SUPPORT_FEEDBACK_TEXT_MAX_LENGTH,
                    required=True,
                ),
            ],
        )
        self.support_id = support_id
        self.author_id = author_id
        self.guild = guild

    async def callback(self, inter: ModalInteraction) -> None:
        support_feedback_text = inter.text_values["support_feedback_text"]
        async with session_factory() as session:
            if guild_settings := await get_guild_settings(session, guild_id=self.guild.id):
                await send_support_feedback(
                    session,
                    guild=self.guild,
                    guild_settings=guild_settings,
                    author_discord_id=self.author_id,
                    support_discord_id=self.support_id,
                    text=support_feedback_text,
                )
                await inter.response.send_message(embed=SupportFeedbackHasSentEmbed(support_id=self.support_id, text=support_feedback_text))
