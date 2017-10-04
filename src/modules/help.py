# coding=utf-8
import discord
from discord.ext import commands
import src.modules.Paginator as Pg
import discord.colour as colors

__author__ = "Luke"
__version__ = "0.0.1"


class Help:
    """Shows this message."""

    def __init__(self, bot):
        self.bot = bot

        self.help_message = ""

    @commands.command(pass_context=True, no_pm=True)
    async def help(self, ctx):
        fields = [Pg.Field(name="bob", short_description="bob was here",
                           long_description="heyo bitches bob is here")]

        self.help_message = Pg.Paginator(self.bot, ctx.message, colour=colors.Color.blue(), title="Help",
                                         description="HEHEHEHEHEHE", fields=fields)

        await self.help_message.start()


def add_to_bot(bot):
    bot.add_cog(Help(bot))
    print("help Added to Bot!")


def remove_from_bot(bot):
    bot.remove_cog("Help")
    print("help Removed From Bot")