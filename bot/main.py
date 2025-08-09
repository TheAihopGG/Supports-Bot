from disnake.ext import commands
from disnake import Intents

from core.configuration import BOT_TOKEN


bot = commands.InteractionBot(
    intents=Intents(),
)
bot.run(BOT_TOKEN)
