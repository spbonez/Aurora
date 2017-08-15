# coding=utf-8
import discord.permissions as perm
import discord.utils as util
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
                          "ireland", "israel", "italy",
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

    @commands.command(pass_context=True, no_pm=True)
    async def join(self, ctx, country: str):
        if country in self.countries:
            country_role = util.get(ctx.message.server.roles, name=country)
            if country_role is not None:
                await self.bot.add_roles(ctx.message.author, country_role)
            else:
                country_role = await self.bot.create_role(ctx.message.server, name=country,
                                                          permissions=perm.Permissions.none())
                await self.bot.add_roles(ctx.message.author, country_role)

            await self.bot.say("{0.author.mention} you have been assigned to {1}".format(ctx.message, country_role))

    async def leave(self, country: str):
        pass

    @commands.command(pass_context=False, no_pm=True)
    async def roles(self):
        msg = 'Region Roles\n' \
              'To join a region use the join command followed by the desired region'
        msg += "```"
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
