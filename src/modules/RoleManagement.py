# coding=utf-8
import discord
from discord.ext import commands


class RoleManagement:
    def __init__(self, bot):
        self.bot = bot
        self.active = False
        self.countries = {}

    @commands.command(pass_context=True, no_pm=True)
    async def activate_roles(self, ctx):

        def check(msg):
            if msg.content == 'std' or msg.content == 'custom':
                return True
            else:
                return False

        if ctx.message.author is ctx.message.server.owner and not self.active:
            await self.bot.say("Use the standard county list, or a custom list ? (std / custom)")

            msg = await self.bot.wait_for_message(timeout=30, author=ctx.message.author, channel=ctx.message.channel,
                                                  check=check)
            if msg is not None:
                await self.bot.say("What up")

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
