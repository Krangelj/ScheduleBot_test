import discord
from discord.ext import commands
from apscheduler.schedulers.async_ import AsyncScheduler
from apscheduler.triggers.date import DateTrigger
from datetime import datetime, timedelta


class Management(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.scheduler = AsyncScheduler()

    @commands.Cog.listener()
    async def on_ready(self):
        """Function which inits the scheduler as the bot is ready
        """
        await self.scheduler.__aenter__()

    async def reply_task(self, message: discord.Message, description: str):
        """This function gets invoked by the scheduler
        Args:
            message(discord.Message): Message to reply to
            description(str):   Message that should get displayed 10 seconds after
        """
        await message.reply(description)

    @commands.command(name='test')
    async def command_test(self, ctx: commands.Context, *, description: str):
        """ This is a function which based on the provided information
        will start to execute 10 seconds after it got called.

         Args:
             ctx(commands.Context): Current context in which the message got invoked
             description(str): Message that should get displayed 10 seconds after
         Returns:
             str: Command
        """
        trigger = DateTrigger(datetime.now() + timedelta(seconds=10))
        await self.scheduler.add_schedule(
            self.reply_task, args=[ctx.message, description],
            trigger=trigger
        )


def setup(bot: commands.Bot):
    bot.add_cog(Management(bot))