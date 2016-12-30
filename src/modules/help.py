import json
import src.permission as perm
Helper = {
    '!help':{'Help':'!help [!command]', 'Description':'display usage and description', 'Type':'User'}
}
async def help(client, message, *args):
    useage = "**Usage:**\n"
    description = "**Description:**\n"
    cmd = args[0]
    if cmd == '':
        cmd='!help'
    with open('../config/config.json', 'r') as json_file:
        data = json.load(json_file)
    json_file.close()

    cmds = data['Helper']
    if cmd in cmds:
        if cmds[cmd]['Help']=='':
            helpmessage = 'Sorry. But the requested Command got no help information.'
        else:
            if cmds[cmd]['Type']=='Admin' and await perm.have_permission(message.author) == 2 :
                helpmessage =useage+ "```"+ cmds[cmd]['Help'] + "```\n" + description+"```"+cmds[cmd]['Description']+"```"+"\n**Type of Command:**\n```"+cmds[cmd]['Type']+" Command```"
            elif cmds[cmd]['Type']=='User':
                helpmessage = useage + "```" + cmds[cmd]['Help'] + "```\n" + description + "```" + cmds[cmd]['Description'] + "```" + "\n**Type of command:**\n```" + cmds[cmd]['Type'] + " command```"
            elif cmds[cmd]['Type']=='Game':
                helpmessage = useage + "```" + cmds[cmd]['Help'] + "```\n" + description + "```" + cmds[cmd]['Description'] + "```" + "\n**Type of command:**\n```" + cmds[cmd]['Type'] + " command```"
            else:
                helpmessage = 'Sorry. That Command is for Administrators only only'
    else:
        helpmessage = 'Sorry. But the requested Command is not found'
    await client.send_message(message.channel, helpmessage)