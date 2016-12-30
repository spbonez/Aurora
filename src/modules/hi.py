Helper = {
    '!hi': {'Help': '!hi', 'Description': 'displays hi', 'Type': 'User'},
    '!roger': {'Help': '!roger', 'Description': 'Roger Roger', 'Type': 'User'},
    '!sage': {'Help': '!sage', 'Description': 'Sage favorite show', 'Type': 'User'}
}
async def hi(client, message, *args):
    await client.send_message(message.channel, 'Hi!')

async def roger(client, message, args):
    file = '../img/rogerroger.png'
    await client.send_file(message.channel, file)

async def sage(client, message, args):
    file = '../img/MLP.jpg'
    await client.send_file(message.channel, file)