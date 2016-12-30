import json
import src.permission as perm
Helper = {
    '!list':{'Help':'!list', 'Description':'lists the commands', 'Type':'User'}
}
async def list(client, message, args):
    with open('../config/config.json', 'r') as json_file:
        data = json.load(json_file)
    json_file.close()
    admincmds = data['Commands']['Admin_Cmd']
    usercmds = data['Commands']['User_Cmd']
    gamecmds = data['Commands']['Game_Cmd']
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

    GameCommand = str(gamecmds)
    GameCommand = GameCommand.replace('[', '')
    GameCommand = GameCommand.replace(']', '')
    GameCommand = GameCommand.replace("'", "")
    GameCommands = GameCommand.replace(', ', '\n')

    print(admincmds)
    print(usercmds)
    if await perm.have_permission(message.author) == 2:
        await client.send_message(message.channel,  '**Admin Commands:**\n```' + AdminCommands +
                                                    '```\n**User Commands:**\n```'+UserCommands+
                                                    '```\n**Game Commands:**\n```' + GameCommands + '```')
    else:
        await client.send_message(message.channel,  '**User Commands:**\n```' + UserCommands +
                                                    '```\n**Game Commands:**\n```' + GameCommands + '```')