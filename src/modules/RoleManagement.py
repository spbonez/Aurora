# coding=utf-8
import discord
from discord.ext import commands


class RoleManagement:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def activate_roles(self, ctx, *, user: discord.Message.author):
        if user is user:
            print("YES!")

    async def assign_role(self):
        pass

    async def remove_role(self):
        pass


def add_to_bot(bot):
    bot.add_cog(RoleManagement(bot))
    print("Role Management Added to Bot!")


def remove_from_bot(bot):
    bot.remove_cog("RoleManagement")
    print("Role Management Removed From Bot")
