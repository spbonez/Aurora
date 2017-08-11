# coding=utf-8
import asyncio
import discord
from discord.ext import commands


class Watcher:

    bot = commands.Bot

    def __init__(self, DiscordBot):
        global bot
        bot = DiscordBot

    @bot.event()
    def on_message(message):
        print(message)
