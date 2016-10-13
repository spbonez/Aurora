import discord

async def mute(client, message, arg):
    string = arg.split(' ')

    # Get the members ID
    member_id = string[0]
    member_id = member_id.replace('<', '')
    member_id = member_id.replace('@', '')
    member_id = member_id.replace('>', '')

    # Find the mute role
    for server in client.servers:
        print(server)
        for roles in server.roles:
            print(roles.name)
            if roles.name == 'Muted':
                role = roles

                # Find the member using the ID
                members = client.get_all_members()
                for member in members:
                    print('Current id:', member.id, '| our member id:', member_id)
                    if member.id == member_id:
                        # Mute the member
                        print('did it')
                        await client.add_roles(member, role)
                        break
