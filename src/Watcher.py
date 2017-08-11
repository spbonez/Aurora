# coding=utf-8
import asyncio
import discord
from discord.ext import commands


class Watcher:

    @staticmethod
    async def new_message(message):
        Logger.log_to_console(message)


class Logger:
    @staticmethod
    async def log_to_console(message):
        print(str(message.server) + " | " + str(message.channel) + " | " + str(message.author) + " - "
              + str(message.content))
