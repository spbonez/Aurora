# coding=utf-8
import asyncio
import discord
from discord.ext import commands


class Watcher:

    def __init__(self, bot):
        self.bot = bot


    @bot.event()
    def on_message(message):
        print(message)
