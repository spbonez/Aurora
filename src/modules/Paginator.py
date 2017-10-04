# coding=utf-8
import discord.embeds as embed
import discord.colour as colors

__author__ = "Luke"
__version__ = "0.0.1"


class Field:
    def __init__(self, **kwargs):
        self.parent = kwargs.get("parent", None)
        self.name = kwargs.get("name", "N/A")
        self.value = kwargs.get("short_description", "")
        self.description = kwargs.get("long_description", "")
        self.fields = kwargs.get("fields", None)


Cog = Field

'''
class FieldItem(Field):
    def __init__(self, parent: embed.Embed, *, name: str, short_description: str, long_description: str):
        super().__init__(parent, name=name, short_description=short_description, long_description=long_description)


Command = FieldItem'''


class Paginator:
    def __init__(self, bot, msg, **kwargs):
        self.bot = bot
        self.msg = msg

        try:
            colour = kwargs['colour']
        except KeyError:
            colour = kwargs.get('color', embed.EmptyEmbed)

        self.colour = colour
        self.title = kwargs.get('title', embed.EmptyEmbed)
        self.type = kwargs.get('type', 'rich')
        self.url = kwargs.get('url', embed.EmptyEmbed)
        self.description = kwargs.get('description', embed.EmptyEmbed)
        self.fields = kwargs.get('fields', None)
        self.main_page = self.__create_page(self.title, self.description, colour, self.fields)
        self.pages = {}
        self.running = True
        self.active_emoji = '📜'
        self.emojies = {
            'right': '➡',
            'left': '⬅',
            'goto': ':1234:',
            1: ':one:',
            2: ':two:',
            3: ':three:',
            4: ':four:',
            5: ':five:',
            6: ':six:',
            7: ':seven:',
            8: ':eight:',
            9: ':nine:',
            10: '🔟',
            'bin': '🗑',
            'settings': '⚙',
        }

        for field in self.fields:
            field.parent = self.main_page

    def add_page(self, page: embed.Embed):
        self.pages[page.title] = page

    def remove_page(self, page: embed.Embed):
        self.pages.pop(page.title)

    def __create_page(self, title: str, description: str, colour: colors.Color, fields: [] = None):
        page = embed.Embed(title=title, description=description, colour=colour, timestamp=self.msg.timestamp)
        page.set_author(name='Requested by: ' + self.msg.author.name + '#' + self.msg.author.discriminator,
                        icon_url=self.msg.author.avatar_url)
        if fields is None:
            pass
        else:
            for idx, field in enumerate(fields):
                page.add_field(name=str("__**"+field.name+"**__"), value=field.value)
        return page

    async def start(self):
        await self.bot.add_reaction(self.msg, self.active_emoji)
        await self.bot.wait_for_reaction(emoji=self.active_emoji, user=self.msg.author, message=self.msg)
        await self.bot.delete_message(self.msg)
        page = await self.bot.say(embed=self.main_page)

        '''for emoji in self.emojies:
            await self.bot.add_reaction(page, emoji)

        while self.running:
            def check(msg):
                for rea in msg.reactions:
                    if rea.count > 1 and rea.emoji in self.emojies.items():
                        pass

            def action(em):
                for key, value in self.emojies:
                    if em == value:
                        return key

            selcted = action(await self.bot.wait_for_reaction(user=self.msg.author, message=page, check=check))'''


