# coding=utf-8
import discord
from discord.ext import commands


class AFK:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def afk(self, ctx):
        await self.bot.change_nickname(ctx.message.author, "bob")


def add_to_bot(bot):
    bot.add_cog(AFK(bot))
    print("AFK Added to Bot!")


def remove_from_bot(bot):
    bot.remove_cog("AFK")
    print("AFK Removed From Bot")