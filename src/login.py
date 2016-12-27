import discord

from config.auth import user
import src.CommandProcessor as CP
import src.permission as perm


class bot:
    # Define Bot Init to the use of self.
    def __init__(self):
        # self.commands = dir to commands
        # self.prefix = dir to prefix
        self.Token = user.Token

    def start(self):
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
            CP.begin(client)

        @client.event
        async def on_server_join(server):
            await perm.first_run(client, server)

        client.run(self.Token)

bot().start()
