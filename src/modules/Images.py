# coding=utf-8
from discord.ext import commands
from discord import embeds
from discord import colour
import requests
import xml.etree.ElementTree as ET
import random
import os
from config.auth import CatAPI


__author__ = "Luke"
__version__ = "1.0.0"


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
    async def dog(self, ctx):
        base_url = "http://api.thedogapi.co.uk/v2/dog.php"

        r = requests.get(base_url).json()
        picture_url = r['data'][0]['url']

        em = embeds.Embed(color=colour.Color.blue())
        em.set_image(url=picture_url)

        await self.bot.say(embed=em)

    @images.command(pass_context=True)
    async def cat(self, ctx, category: str = None):

        if len(str(ctx.invoked_subcommand)) <= 10:
            base_url = "http://thecatapi.com/api/images/get"
            payload = {'api_key': CatAPI.key, 'format': 'xml', 'type': 'jpg,png'}

            if category is not None:
                payload['category'] = category
            if category == "categories" or category == "list":
                await self.categories()
            else:
                try:
                    r = requests.get(base_url, payload)

                    root = ET.fromstring(str(r.text))
                    picture_url = root[0][0][0][0].text

                    em = embeds.Embed(color=colour.Color.blue())
                    em.set_image(url=picture_url)

                    await self.bot.say(embed=em)

                except IndexError:
                    await self.bot.say(self.not_found())

    async def categories(self):
        base_url = "http://thecatapi.com/api/categories/list"
        r = requests.get(base_url)

        root = ET.fromstring(str(r.text))

        description = ""

        for category in root.iter('category'):
            description += str(category[1].text) + "\n"

        em = embeds.Embed(color=colour.Color.blue(), title="Cats Categories", description=description)

        await self.bot.say(embed=em)

    @images.command(pass_context=True)
    async def beer(self, ctx):
        path = os.path.join(os.getcwd(), "data", "img", "beers")
        beers = os.listdir(path)
        min = 1
        max = len(beers)
        number = random.randint(min, max)
        path = os.path.join(path, "beer")
        file = path + str(number) + '.jpg'

        await self.bot.send_file(ctx.message.channel, file)

    @staticmethod
    def not_found():

        messages = ["I'm sorry Dave, I'm afraid I can't do that", "It can only be attributable to human error.",
                    "Just what do you think you're doing, Dave?", "400 Bad Request",
                    "406 Not Acceptable", "418 I'm a teapot", "450 Blocked by Windows Parental",
                    "204 No Content", "OMG seriously? You want me to do that?", "Human Error, sure you belong here?",
                    "Sure you spelled that right?", "An error occurred while displaying the previous error",
                    "Lol I can't be bothered with that right now", "plz press Alt + F4 to continue",
                    "Operation completed, but that doesn’t mean it’s error free.",
                    "You have not gotten any error messages recently, so here is a random one just to let you know we "
                    "havnet started caring", "DISCORD_SendMessage ERROR: NO ERROR", "Something bad happened",
                    "Your TV is lonely", "Catastrophic Failure", "how about you give me a candle light dinner first",
                    "User error, Replace user", "sorry you had too much. I am cutting you off",
                    "Error code 42: User error, its not our fault!", "Hello there!... Oh it's just you",
                    "You type like i drive", "Where did you learn to type?",
                    "Are you on drugs?", "stty: unknown mode: doofus", "You do that again and see what happens...",
                    "What, what, what, what, what, what, what, what, what, what?",
                    "Speak English you fool --- there are no subtitles in this scene.",
                    "My pet ferret can type better than you!", "Maybe if you used more than just two fingers...",
                    "I've seen penguins that can type better than that."]

        return random.choice(messages)


def add_to_bot(bot):
    bot.add_cog(Images(bot))
    print("Images Added to Bot!")


def remove_from_bot(bot):
    bot.remove_cog("Images")
    print("Images Removed From Bot")
