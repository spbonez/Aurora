# coding=utf-8
from discord.ext import commands
import random
from data.facts.fucked import facts

__author__ = "Luke"
__version__ = "0.0.1"


class Facts:
    """Facts about stuff."""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def facts(self, ctx):
        """Marhhh"""
        if ctx.invoked_subcommand is None:
            # Display Facts help page.
            return

    @facts.command(pass_context=True)
    async def strange(self, ctx):
        await self.bot.say(random.choice(facts))


def add_to_bot(bot):
    bot.add_cog(Facts(bot))
    print("Facts Added to Bot!")


def remove_from_bot(bot):
    bot.remove_cog("Facts")
    print("Facts Removed From Bot")
