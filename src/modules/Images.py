# coding=utf-8
from discord.ext import commands
import urllib.request as request
from xml.etree import ElementTree
from config.auth import CatAPI


__author__ = "Luke"
__version__ = "0.0.1"


class Images:

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def images(self, ctx):
        """Marhhh"""
        if ctx.invoked_subcommand is None:
            # Display Facts help page.
            return

    @images.command(pass_context=True)
    async def cat(self, ctx):
        base_url = "http://thecatapi.com/api/images/get?response=xml"
        payload = {'response': 'src'}

        r = request.urlopen(base_url).read()
        tree = ElementTree.fromstring(r)
        print(str(tree))



def add_to_bot(bot):
    bot.add_cog(Images(bot))
    print("Images Added to Bot!")


def remove_from_bot(bot):
    bot.remove_cog("Images")
    print("Images Removed From Bot")
