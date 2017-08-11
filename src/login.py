# coding=utf-8
from src import Commands
import os
from discord.ext import commands
from config.auth import User
from src.Watcher import Watcher

modulePath = os.path.join(os.getcwd(), "src", "modules")

bot = commands.Bot(command_prefix=commands.when_mentioned_or('§'), description='AuroraV2 DevBuild PreAlpha')
Commands.load_all_modules(modulePath, bot)


@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))


@bot.event
async def on_message(message):
    Watcher.new_message(message)

bot.run(User.Token)

