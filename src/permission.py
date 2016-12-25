import json
import discord.utils as utils
import asyncio

Bot_Name = 'FlixBot'
Admin_Name = 'Flixbot Admin.'
Muted = 'Muted'
Everyone = '@everyone'

async def first_run(client, new_server):

    print('New Server was joined! \n', new_server)

    with open('../config/config.json', 'r') as json_file:
        data = json.load(json_file)
    json_file.close()

    Bot_Role = utils.get(new_server.roles, name=Bot_Name)
    await client.create_role(new_server, name=Admin_Name)
    await asyncio.sleep(3)

    data['Servers'][str(new_server)] = {}

    for roles in new_server.roles:
        if str(roles.name) == Admin_Name \
                or str(roles.name) == Everyone \
                or str(roles.name) == Muted \
                or str(roles.name) == str(Bot_Role.name):
            data['Servers'][str(new_server)][str(roles.name)] = roles.id

    with open('../config/config.json', 'w') as json_data:
        json.dump(data, json_data, indent=2)
    json_data.close()

async def have_permission(user):
    if utils.get(user.roles, name=Admin_Name) is not None:
        return 2
    elif utils.get(user.roles, name=Muted) is not None:
        return 0
    elif utils.get(user.roles, name=Everyone) is not None:
        return 1
