import discord

async def mute(client, message, arg):
    string = arg.split(' ')

    # Get the members ID
    member_id = string[0]
    member_id = member_id.replace('<', '')
    member_id = member_id.replace('@', '')
    member_id = member_id.replace('>', '')

    # Find the mute role
    roles = client.roles
    for role in roles:
        print(role)

    # Find the member using the ID
    members = client.get_all_members()
    for member in members:
        if member.id == member_id:
            # Mute the member
            # await client.add_roles(member, 'Muted')
            break
