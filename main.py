import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

Bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('$$')
)

Bot.load_extension('cogs.daily_question')

Bot.run(os.getenv('DISCORD_TOKEN'))