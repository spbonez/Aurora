import src.permission as perm
import json
Helper = {
    '!join':{'Help':'!join [rolename] or !join [rolename] [rolename] and so on', 'Description':'adds a cosmetic role to you, you can add multuple roles at the same time', 'Type':'User'},
    '!addlockedrole':{'Help':'!addlockedrole [rolename] or !addlockedrole [rolename] [rolename] and so on', 'Description':'locks a role or multiple roles from join', 'Type':'Admin'},
    '!showroles':{'Help':'!showroles', 'Description':'!shows the available roles', 'Type':'User'},
    '!leave':{'Help':'!leave [rolename] or !leave [rolename] [rolename] and so on', 'Description':'leaves the cosmetic role or roles', 'Type':'User'}
}
async def join(client, message, arg):
    arg = arg.split(',')
    args = []
    for v in arg:
        if v.startswith(' '):
            args.append(v[1:])
        else:
            args.append(v)
    print(args)

    with open('../config/config.json', 'r') as json_file:
        data = json.load(json_file)

    def check(msg):
        if msg.content == '#Agree' or msg.content == '#agree':
            return True
        else:
            return False

    for role in message.server.roles:
        if str(role.name.lower()) in args \
                and str(role.name.lower()) not in data['Servers'][str(message.server)]['Locked_Roles'] \
                and str(role.name.lower()) != 'mature/nsfw(18+)':
            await client.add_roles(message.author, role)
        elif str(role.name.lower()) in data['Servers'][str(message.server)]['Locked_Roles'] \
                and str(role.name.lower()) in args:
            await client.send_message(message.channel, role.name + ' requires admin approval')
        elif str(role.name.lower()) == 'mature/nsfw(18+)':
            await client.send_message(message.channel, 'By joining this role you accept you are at least 18 years old.'
                                                       '\nType #Agree to accept the term')
            msg = await client.wait_for_message(timeout=30, author=message.author, channel=message.channel, check=check)
            if msg is not None:
                await client.send_message(message.channel, 'You have now joined ' + str(role.name))
                await client.add_roles(message.author, role)
            else:
                await client.send_message(message.channel, 'Your time have ended!')


async def addlockedrole(client, message, arg):

    if await perm.have_permission(message.author) == 2:
        arg = arg.split(',')
        args = []
        for v in arg:
            if v.startswith(' '):
                args.append(v[1:])
            else:
                args.append(v)
        print(args)

        with open('../config/config.json', 'r') as json_file:
            data = json.load(json_file)
        json_file.close()

        with open('../config/config.json', 'w') as json_file:
            for role in message.server.roles:
                if str(role.name.lower()) in args:
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
    for v in arg:
        if v.startswith(' '):
            v = v[1:]

    with open('../config/config.json', 'r') as json_file:
        data = json.load(json_file)
    json_file.close()

    for role in message.server.roles:
        if str(role.name.lower()) in arg \
                and str(role.name) not in data['Servers'][str(message.server)]['Locked_Roles']:
            await client.remove_roles(message.author, role)

