Helper = {
    '!roger': {'Help': '!roger', 'Description': 'Roger Roger', 'Type': 'User'},
    '!sage': {'Help': '!sage', 'Description': 'Sage favorite show', 'Type': 'User'},
    '!magnets': {'Help': '!magnets', 'Description': 'Reason: MAGNETS!', 'Type': 'User'}
}
async def roger(client, message, args):
    file = '../img/memes/rogerroger.png'
    await client.send_file(message.channel, file)

async def sage(client, message, args):
    file = '../img/memes/sage.jpg'
    await client.send_file(message.channel, file)

async def magnets(client, message, args):
    file = '../img/memes/magnets.gif'
    await client.send_file(message.channel, file)