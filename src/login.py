import src.modules as modules
from src.modules import music
import asyncio
import discord
from discord.ext import commands

from config.auth import User

bot = commands.Bot(command_prefix=commands.when_mentioned_or('§'), description='A playlist example for discord.py')

getattr(modules, "add_to_bot")(bot)


@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

bot.run(User.Token)
