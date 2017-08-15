# coding=utf-8
import discord.utils as utilis
from discord.ext import commands


class AFK:
    def __init__(self, bot):
        self.bot = bot
        self.afk_members = []

    @commands.command(pass_context=True, no_pm=True)
    async def afk(self, ctx):
        self.afk_members.append(ctx.message.author)
        print(self.afk_members)
        await self.bot.change_nickname(ctx.message.author, "bob")

    # Afk member messaged
    async def message_watcher(self):

        def check(msg):
            print(msg.mentions + '--------------' + self.afk_members)
            if msg.mentions in self.afk_members:
                return True
            else:
                return False

        if self.afk_members.count > 0:
            msg = await self.bot.wait_for_message(check=check)

            if msg is not None:
                await self.bot.say("bob")


def add_to_bot(bot):
    afk = AFK(bot)
    afk.message_watcher()
    bot.add_cog(afk)
    print("AFK Added to Bot!")


def remove_from_bot(bot):
    bot.remove_cog("AFK")
    print("AFK Removed From Bot")
