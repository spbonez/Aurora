# coding=utf-8
import discord
from discord.ext import commands


class AFK:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def afk(self, ctx):
        self.bot.change_nickname(ctx.message.author, str("[AFK]" + ctx.message.author.nick))


def add_to_bot(bot):
    bot.add_cog(AFK(bot))
    print("AFK Added to Bot!")


def remove_from_bot(bot):
    bot.remove_cog("AFK")
    print("AFK Removed From Bot")