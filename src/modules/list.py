import json
import src.permission as perm
async def list(client, message, args):
    with open('../config/config.json', 'r') as json_file:
        data = json.load(json_file)
    json_file.close()
    admincmds = data['Commands']['Admin_Cmd']
    usercmds = data['Commands']['User_Cmd']
    AdminCommand = str(admincmds)
    AdminCommand = AdminCommand.replace('[', '')
    AdminCommand = AdminCommand.replace(']', '')
    AdminCommand = AdminCommand.replace("'", "")
    AdminCommands = AdminCommand.replace(', ', '\n')

    UserCommand = str(usercmds)
    UserCommand = UserCommand.replace('[', '')
    UserCommand = UserCommand.replace(']', '')
    UserCommand = UserCommand.replace("'", "")
    UserCommands = UserCommand.replace(', ', '\n')

    print(admincmds)
    print(usercmds)
    if await perm.have_permission(message.author) == 2:
        await client.send_message(message.channel, '**Admin Commands:**\n```' + AdminCommands + '```\n**User Commands:**\n```'+UserCommands+'```')
    else:
        await client.send_message(message.channel, '**User Commands:**\n```' + UserCommands + '```')