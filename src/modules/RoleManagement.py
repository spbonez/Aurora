# coding=utf-8
import discord
from discord.ext import commands


class RoleManagement:
    def __init__(self, bot):
        self.bot = bot
        self.active = False
        self.countries = {"{US}pacific", "{US}central", "{US}eastern", "{US}mountain",
                          "africa", "asia", "australia", "austria",
                          "belgium", "bosnia", "brazil", "bulgaria",
                          "canada", "croatia", "czech",
                          "denmark",
                          "estonia", "europe",
                          "finland", "france",
                          "germany", "greece",
                          "hungary",
                          "ireland",  "israel", "italy",
                          "latvia", "lithuania",
                          "macedonia", "mexico", "middle_east",
                          "netherlands", "norway", "newzealand",
                          "philippines", "poland", "portugal",
                          "romania", "russia",
                          "saudi", "scotland", "serbia", "singapore", "slovakia", "slovenia",
                          "southamerica", "spain", "sweden", "switzerland",
                          "turkey",
                          "unitedkingdom"
                          }

    async def join(self, country: str):
        pass

    async def leave(self, country: str):
        pass

    @commands.command(pass_context=False, no_pm=True)
    async def show(self):
        msg = "```"
        for country in sorted(self.countries):
            msg += country + "\n"
        msg += "```"
        await self.bot.say(msg)


def add_to_bot(bot):
    bot.add_cog(RoleManagement(bot))
    print("Role Management Added to Bot!")


def remove_from_bot(bot):
    bot.remove_cog("RoleManagement")
    print("Role Management Removed From Bot")
