import json
import os
from asyncio import sleep
import discord.utils as utils
from src.permission import Admin_Name

async def first_run(client, new_server):

    print('New Server was joined! \n', new_server)
    # await client.create_role(new_server, name=Admin_Name)

    if os.stat('../config/config.json').st_size > 0:
        with open('../config/config.json', 'r') as json_file:
            data = json.load(json_file)
        json_file.close()

        with open('../config/config.json', 'w') as json_file:
            data['Servers'][str(new_server)] = {'Roles': {}, 'Locked_Roles': {}}
            for role in new_server.roles:
                data['Servers'][str(new_server)]['Roles'][str(role.name.lower())] = str(role.name)

            json.dump(data, json_file, indent=2, sort_keys=True)
        json_file.close()
    else:
        data = {'Servers': {}}
        data['Servers'][str(new_server)] = {'Roles': {}, 'Locked_Roles': {}}

        for role in new_server.roles:
            data['Servers'][str(new_server)]['Roles'][str(role.name.lower())] = str(role.name)

        with open('../config/config.json', 'w') as json_file:
            json.dump(data, json_file, indent=2, sort_keys=True)
        json_file.close()


async def new_role(role):
    await sleep(15)
    print('New role added:', role.name, role.server)
    with open('../config/config.json', 'r') as json_file:
        data = json.load(json_file)
    json_file.close()
    with open('../config/config.json', 'w') as json_file:
        data['Servers'][str(role.server)]['Roles'][str(role.name.lower())] = str(role.name)
        json.dump(data, json_file, indent=2, sort_keys=True)
    json_file.close()






