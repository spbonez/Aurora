import discord

from config.auth import user
Token = user.Token

client = discord.Client()


@client.event
async def on_ready():
    print('\nLogged in successfully')
    print('User Name:   ', client.user.name)
    print('User ID:     ', client.user.id)
    print('Connected Servers:')
    for server in client.servers:
        print(server)
    print('------------------')

client.run(auth.user.Token)
