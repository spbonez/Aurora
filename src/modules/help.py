async def help(client, message, *args):
    useage = 'Usage:\n'
    description = 'Description:\n'
    cmd = args[0]

    if cmd == 'ban':
        helptext = '```\n!' + cmd + ' [@user] [Message]\n```'
        destext = '```\n[!' + cmd + '] bans a member, a reason will be sent to the member\n```'
    elif cmd == 'hi':
        helptext = '```\n!' + cmd + '\n```'
        destext = '```\n[!' + cmd + '] bot replies with a hi\n```'
    elif cmd == 'info':
        helptext = '```\n!' + cmd + '\n!' + cmd + ' Update [Message]```'
        destext = '```\n[!' + cmd + '] shows or updates the bot info\n```'
    elif cmd == 'kick':
        helptext = '```\n!' + cmd + ' [@user] [Message]\n```'
        destext = '```\n[!' + cmd + '] kicks a member, a reason will be sent to the member\n```'
    elif cmd == 'mute':
        helptext = '```\n!' + cmd + ' [@user]\n```'
        destext = '```\n[!' + cmd + '] mutes a member\n```'
    elif cmd == 'roll':
        helptext = '```\n!' + cmd + '\n```'
        destext = '```\n[!' + cmd + '] rolls a dice from 1 to 6\n```'
    elif cmd == 'list':
        helptext = '```\n!' + cmd + '\n```'
        destext = '```\n[!' + cmd + '] list the available commands\n```'
    else:
        helptext= '```\n!help [command_name]\n !\n```'
        destext= '```\n[!help] display the Usage and Description of the command\n```'

    helpmessage = useage + helptext + description + destext
    await client.send_message(message.channel, helpmessage)