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
        await self.bot.change_nickname(ctx.message.author, str("[AFK]" + str(ctx.message.author.nick)))
        await self.message_watcher(ctx.message.author)

    @commands.command(pass_context=True, no_pm=True)
    async def back(self, ctx):
        self.afk_return(ctx.message.author)

    # Afk member messaged
    async def message_watcher(self, user):

        def check(message):
            print(message.mentions)
            print("--------------")
            print(self.afk_members)
            if user in message.mentions:
                return True
            elif user is message.author:
                self.afk_return(user)
                return True
            else:
                return False

        while user in self.afk_members:
            msg = await self.bot.wait_for_message(check=check)

            if msg is not None:
                if user in self.afk_members:
                    await self.bot.say(user.nick + " is afk")
                else:
                    await self.bot.say("Welcome back " + str(msg.author.nick))

    def afk_return(self, member):
        self.afk_members.remove(member)
        self.bot.change_nickname(member, None)


def add_to_bot(bot):
    bot.add_cog(AFK(bot))
    print("AFK Added to Bot!")


def remove_from_bot(bot):
    bot.remove_cog("AFK")
    print("AFK Removed From Bot")
