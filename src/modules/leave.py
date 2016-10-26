import src.permission as perm

async def leave(client, message, *argument):
    if await perm.have_access(message.author) == perm.Roles.Admin.Level:
        await client.leave_server(message.server)
    else:
        await client.send_message(message.channel, 'This command is only available for ' + perm.Roles.Admin.Name + 's')