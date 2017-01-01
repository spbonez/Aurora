Helper = {
    '!hi': {'Help': '!hi', 'Description': 'displays hi', 'Type': 'User'}
}
async def hi(client, message, *args):
    await client.send_message(message.channel, 'Hi!')