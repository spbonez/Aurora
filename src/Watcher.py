# coding=utf-8
import asyncio
import discord
from discord.ext import commands


class Watcher:

    @staticmethod
    def new_message(message):
        print(str(message.server) + " | " + str(message.channel) + " | " + str(message.author) + " - "
              + str(message.content))
