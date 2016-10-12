import discord

async def kick(client, message, arg):
    string = arg.split(' ')

    # Get the members ID
    member_id = string[0]
    member_id = member_id.replace('<', '')
    member_id = member_id.replace('@', '')
    member_id = member_id.replace('>', '')

    # Remove the ID and combine back to string
    del string[0]
    reason = ' '.join(string)

    # Find the member using the ID
    members = client.get_all_members()
    for member in members:
        if member.id == member_id:
            # Send message to the user, with the reason to the kick
            await client.send_message(member, 'You have been kicked from KvasigSG Development\n'
                                              'Reason for your kick: ```' + reason + '```')
            # Kick the member
            await client.send_message(message.channel, '' + member.name + ' was kicked, and a personal message'
                                                                ' was sent to him/her with the '
                                                                'reason: ```' + reason + '```')
            await client.kick(member)
            break
