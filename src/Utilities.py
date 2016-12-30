import json
import os
from asyncio import sleep
import discord.utils as utils
from src.permission import Admin_Name

async def first_run(client, new_server):

    print('New Server was joined! \n', new_server)
    await client.create_role(new_server, name=Admin_Name)

    if os.stat('../config/config.json').st_size > 0:
        with open('../config/config.json', 'r') as json_file:
            data = json.load(json_file)
        json_file.close()

        with open('../config/config.json', 'w') as json_file:
            data['Servers'][str(new_server)] = {'Roles': {}, 'Locked_Roles': {}}
            for role in new_server.roles:
                data['Servers'][str(new_server)]['Roles'][str(role.name.lower())] = str(role.name)
            data['Servers'][str(new_server)]['Locked_Roles'][Admin_Name.lower()] = Admin_Name
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

async def morning_run(client):
    servers = 0
    roles = 0
    with open('../config/config.json', 'r') as json_file:
        data = json.load(json_file)
    json_file.close()

    for server in client.servers:
        if server.name not in data['Servers']:
            servers += 1
            await first_run(client, server)
        else:
            for role in server.roles:
                if role.name.lower() not in data['Servers'][str(server.name)]['Roles']:
                    roles += 1
                    await new_role(role)

    print('Morning Run Finished: %(servers)s new servers, %(roles)s new roles.' % {'servers': servers, 'roles': roles})


