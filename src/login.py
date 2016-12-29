import discord
import src.CommandProcessor as CP
import src.permission as perm
import src.Utilities as utilis
from config.auth import User
import src.Database as database


class Bot:
    # Define Bot Init to the use of self.
    def __init__(self):
        # self.commands = dir to commands
        # self.prefix = dir to prefix
        self.Token = User.Token

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
            database.connect()

        @client.event
        async def on_server_join(server):
            await utilis.first_run(client, server)
            database.new_server(server)

        @client.event
        async def on_server_role_create(role):
            await utilis.new_role(role)

        client.run(self.Token)

Bot().start()
