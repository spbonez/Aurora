import src.Database as database
Helper = {
    '!luke': {'Help': '!bob', 'Description': 'Sage is a moron', 'Type': 'Admin'}
}


async def luke(client, message, arg):
    # user = await database.get(message.server, message.author)
    # database.update(message.server, message.author, ['status'], [1000])
    await client.send_message(message.channel, 'Luke is awesome!')