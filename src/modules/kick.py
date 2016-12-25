import src.permission as perm
import discord.utils as utils

async def kick(client, message, arg):
    if await perm.have_permission(message.author) == 2:
        string = arg.split(' ')

        # Get the members ID
        member_id = string[0]
        member_id = member_id.replace('<', '')
        member_id = member_id.replace('@', '')
        member_id = member_id.replace('>', '')

        # Remove the ID and combine back to string
        del string[0]
        reason = ' '.join(string)

        member = utils.get(message.sever.members, id=member_id)

        # Send message to the user, with the reason to the kick

        await client.send_message(member, 'You have been kicked from ' + message.server.name + '\n'
                                                                                               'Reason for your kick: ```' + reason + '```')
        # Kick the member
        await client.send_message(message.channel, '' + member.name + ' was kicked, and a personal message'
                                                                      ' was sent to him/her with the '
                                                                      'reason: ```' + reason + '```')
        client.kick(member)
    else:
        await client.send_message(message.channel, 'This command is only available for ' + str(perm.Admin_Name) + 's')
