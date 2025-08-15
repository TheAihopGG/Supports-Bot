from ...core.base_embeds import InfoEmbed


class SupportFeedbackEmbed(InfoEmbed):
    def __init__(
        self,
        author_discord_id: int,
        support_discord_id: int,
        text: str,
    ):
        super().__init__()
        self.add_field("Новый отзыв", text)
        self.add_field("От кого", f"<@{author_discord_id}>")
        self.add_field("На кого", f"<@{support_discord_id}>")
