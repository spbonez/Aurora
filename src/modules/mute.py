import src.permission as perm
import discord.utils as utils

async def _mute(client, message, arg):
    if await perm.have_permission(message.author) == 2:
        string = arg.split(' ')

        # Get the members ID
        member_id = string[0]
        member_id = member_id.replace('<', '')
        member_id = member_id.replace('@', '')
        member_id = member_id.replace('>', '')

        muted_role = utils.get(message.server.roles, name='Muted')
        member = utils.get(message.server.members, id=member_id)
        await client.add_roles(member, muted_role)

    else:
        await client.send_message(message.channel, 'This command is only available for ' + str(perm.Admin_Name) + 's')
