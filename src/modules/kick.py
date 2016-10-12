import discord
# not working

async def kick(client, channel, member):
    await client.send_message(channel, 'kicking member')
    await client.kick(member)

