import discord


async def hi(client, message, *args):
    await client.send_message(message.channel, 'Hi!')
