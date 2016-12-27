import src.permission as perm
import discord.utils as utils
import src.Utilities as my_utils

async def join(client, message, arg):
    roles = arg.split(' ')
    restricted_roles = ['bat_member', 'administrator', 'administrative adviser',
                        'flixbot admin.', 'founders', 'selene', 'the twins']

    for role in roles:
        if role in restricted_roles:
            await client.send_message(message.channel, role + ' requires admin approval')

    for role in message.server.roles:
        if str(role.name.lower()) in roles and str(role.name) not in restricted_roles:
            await client.add_roles(message.author, role)

    for server in client.severs:
        await my_utils.RolesTrack().new_server(server)