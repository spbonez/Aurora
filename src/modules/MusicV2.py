import discord
from discord.ext import commands
import threading
import os
import collections

__author__ = "Luke"
__version__ = "0.0.1"

# noinspection PyBroadException
try:
    import youtube_dl
except:
    youtube_dl = None

# noinspection PyBroadException
try:
    if not discord.opus.is_loaded():
        discord.opus.load_opus('libopus-0.dll')
except OSError:
    opus = False
except:  # Missing opus
    opus = None
else:
    opus = True

youtube_dl_options = {
    'source_address': '0.0.0.0',
    'format': 'bestaudio/best',
    'extractaudio': True,
    'audioformat': "mp3",
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'quiet': True,
    'no_warnings': True,
    'outtmpl': "data/audio/cache/%(id)s",
    'default_search': 'auto',
    'encoding': 'utf-8'
}


class Song:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs
        self.title = kwargs.pop('title', None)
        self.id = kwargs.pop('id', None)
        self.url = kwargs.pop('url', None)
        self.webpage_url = kwargs.pop('webpage_url', "")
        self.duration = kwargs.pop('duration', 60)
        self.start_time = kwargs.pop('start_time', None)
        self.end_time = kwargs.pop('end_time', None)


