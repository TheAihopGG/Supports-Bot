from disnake.ext import commands
from disnake import Intents

from bot.core.logger import logger
from bot.core.configuration import BOT_TOKEN
from bot.cogs.guild_settings.cog import GuildSettingsCog
from bot.cogs.verify.cog import VerifyCog
from bot.cogs.help.cog import HelpCog

intents = Intents.default()
intents.members = True
bot = commands.InteractionBot(intents=intents)
[
    bot.add_cog(cog)
    for cog in {
        GuildSettingsCog(),
        VerifyCog(),
        HelpCog(),
    }
]


@bot.event
async def on_ready() -> None:
    logger.info("Bot ready")


bot.run(BOT_TOKEN)
