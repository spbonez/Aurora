import json
import discord.utils as utils
from src.permission import Admin_Name

async def first_run(client, new_server):

    print('New Server was joined! \n', new_server)
    await client.create_role(new_server, name=Admin_Name)


class RolesTrack:

    def new_server(self, new_server):
        with open('../config/config.json') as json_file:
            data = json.load(json_file)

        data['Servers'][str(new_server)]['Roles'] = {}


    def new_role(self):
        print('bob')






