import discord
# from src.modules import *
import src.modules as module


def begin(client):
    @client.event
    async def on_message(message):
        if message.author != client.user:
            print('New message from:', message.author, 'in Channel:', message.channel, '\nContent:', message.content)

        if message.content.startswith('!'):

            msg = message.content.lower().split(' ')
            command = msg[0]
            command = command.replace('!', '')
            del msg[0]
            argument = ' '.join(msg)

            await getattr(module, command)(client, message.channel, argument)
