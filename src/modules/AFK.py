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
        await self.message_watcher(ctx.message.author)

    @commands.command(pass_context=True, no_pm=True)
    async def nick(self, ctx):
        nick = ctx.message.author.nick or ctx.message.author.name
        await self.bot.say(str(nick))

    # Afk member messaged
    async def message_watcher(self, user):
        old_nick = user.nick or user.name
        await self.bot.change_nickname(user, str("[AFK]" + old_nick))

        def check(message):
            print(message.mentions)
            print("--------------")
            print(self.afk_members)
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
                    await self.bot.say(old_nick + " is afk")
                else:
                    await self.bot.change_nickname(user, old_nick)
                    await self.bot.say("Welcome back " + str(old_nick))


def add_to_bot(bot):
    bot.add_cog(AFK(bot))
    print("AFK Added to Bot!")


def remove_from_bot(bot):
    bot.remove_cog("AFK")
    print("AFK Removed From Bot")
