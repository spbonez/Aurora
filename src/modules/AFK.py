# coding=utf-8
import discord
from discord.ext import commands


class AFK:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def afk(self, ctx, status : str):
        self.bot.change_nickname(ctx.message.author, "[AFK]" + ctx.message.author.nick)