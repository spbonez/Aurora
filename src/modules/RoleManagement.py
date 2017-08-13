# coding=utf-8
import discord
from discord.ext import commands


class RoleManagement:
    def __init__(self, bot):
        self.bot = bot
        self.active = False
        self.games = {}
        self.countries = {}

    @commands.command(pass_context=True, no_pm=True)
    async def activate_roles(self, ctx):

        def yes_or_no(msg):
            if msg.content == 'yes' or msg.content == 'Yes':
                return True
            elif msg.content == 'no' or msg.content == 'No':
                return 'nope'

        if ctx.message.author is ctx.message.server.owner and not self.active:
            await self.bot.say("Do you want roles based on games ? ( yes or no)")
            msg = await self.bot.wait_for_message(timeout=30, author=ctx.message.author,
                                                  channel=ctx.message.channel,
                                                  check=yes_or_no)
            if msg is not None or msg is not str:
                await self.bot.say("YAY!")

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
