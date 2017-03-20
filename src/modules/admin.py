import asyncio
import discord
from discord.ext import commands
from src.Commands import update_all_modules
from src.login import modulePath


class AdminCommands:
    """Admin Related Commands.
    If you are not an admin, please dont run these commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=False, no_pm=True, hidden=True)
    async def update_modules(self):
        """Updates all the modules"""
        update_all_modules(modulePath, self.bot)


def add_to_bot(bot):
    bot.add_cog(AdminCommands(bot))
    print("Admin Commands Added to Bot!")


def remove_from_bot(bot):
    bot.remove_cog("AdminCommands")
    print("Admin Commands Removed From Bot")