# coding=utf-8
import discord
from discord.ext import commands


class AFK:
    def __init__(self, bot):
        self.bot = bot
        self.afk_members = []

    @commands.command(pass_context=True, no_pm=True)
    async def afk(self, ctx, *, status: str = ''):
        self.afk_members.append(ctx.message.author)
        await self.bot.say('{0.author.mention} you have been set as AFK'.format(ctx.message))
        await self.message_watcher(ctx.message.author, status)

    @commands.command(pass_context=True, no_pm=True)
    async def nick(self, ctx):
        nick = ctx.message.author.nick or ctx.message.author.name
        await self.bot.say(str(nick))

    # Afk member messaged
    async def message_watcher(self, user, status):
        old_nick = user.nick or user.name
        user_status = status
        await self.bot.change_nickname(user, str("[AFK]" + old_nick))

        def check(message):
            if user in message.mentions:
                return True
            elif user is message.author:
                self.afk_members.remove(user)
                return True
            else:
                return False

        while user in self.afk_members:
            msg = await self.bot.wait_for_message(check=check)

            if msg is not None:
                if user in self.afk_members:
                    await self.bot.send_message(msg.channel, old_nick + " is afk: " + user_status)
                else:
                    await self.bot.change_nickname(user, old_nick)
                    await self.bot.send_message(msg.channel, "Welcome back {0.mention}".format(user))


def add_to_bot(bot):
    bot.add_cog(AFK(bot))
    print("AFK Added to Bot!")


def remove_from_bot(bot):
    bot.remove_cog("AFK")
    print("AFK Removed From Bot")
