import src.permission as perm
import discord.utils as utils
Helper = {
    '!ban':{'Help':'!ban [@User] [Message]', 'Description':'bans a user and sends him a message', 'Type':'Admin'}
}
async def ban(client, message, arg):

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
        # Send message to the user, with the reason to the ban
        await client.send_message(member, 'You have been banned from KvasigSG Development\n'
                                          'Reason for your ban: ```' + reason + '```')
        # ban the member
        await client.send_message(message.channel, '' + member.name + ' was banned, and a personal message'
                                                                      ' was sent to him/her with the '
                                                                      'reason: ```' + reason + '```')
        await client.ban(member, 2)

    else:
        await client.send_message(message.channel, 'This command is only available for ' + str(perm.Admin_Name) + 's')