import src.permission as perm
import json

async def join(client, message, arg):
    arg = arg.split(',')
    arg = [v.replace(' ', '') for v in arg]

    with open('../config/config.json', 'r') as json_file:
        data = json.load(json_file)

    for role in message.server.roles:
        if str(role.name.lower()) in arg \
                and str(role.name.lower()) not in data['Servers'][str(message.server)]['Locked_Roles']:
            await client.add_roles(message.author, role)
        elif str(role.name.lower()) in data['Servers'][str(message.server)]['Locked_Roles']:
            await client.send_message(message.channel, role.name + ' requires admin approval')

async def _addlockedrole(client, message, arg):

    if await perm.have_permission(message.author) == 2:
        arg = arg.split(',')
        arg = [v.replace(' ', '') for v in arg]

        with open('../config/config.json', 'r') as json_file:
            data = json.load(json_file)
        json_file.close()

        with open('../config/config.json', 'w') as json_file:
            for role in message.server.roles:
                if str(role.name.lower()) in arg:
                    data['Servers'][str(message.server)]['Locked_Roles'][str(role.name.lower())] = str(role.name)

            json.dump(data, json_file, indent=2, sort_keys=True)
        json_file.close()
    else:
        await client.send_message(message.channel, 'This command is only available for ' + str(perm.Admin_Name) + 's')

async def showroles(client, message, arg):
    roles = []
    with open('../config/config.json', 'r') as json_file:
        data = json.load(json_file)
    json_file.close()

    for role in data['Servers'][str(message.server)]['Roles']:
        if role not in data['Servers'][str(message.server)]['Locked_Roles']:
            roles.append(data['Servers'][str(message.server)]['Roles'][str(role)])

    roles.sort()
    await client.send_message(message.channel, 'Available Roles are: ```' + '\n'.join(roles) + '```')

async def leave(client, message, arg):
    arg = arg.split(',')
    arg = [v.replace(' ', '') for v in arg]

    with open('../config/config.json', 'r') as json_file:
        data = json.load(json_file)
    json_file.close()

    for role in message.server.roles:
        if str(role.name.lower()) in arg \
                and str(role.name) not in data['Servers'][str(message.server)]['Locked_Roles']:
            await client.remove_roles(message.author, role)

