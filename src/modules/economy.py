import src.Database as database
Helper = {
    '!luke': {'Help': '!bob', 'Description': 'Sage is a moron', 'Type': 'Admin'}
}


async def join_games(client, message, arg):
    user = await database.get(message.server, message.author)

    if user['Status'] == 'Active':
        await client.send_message(message.channel, 'You are all ready joined!')
    else:
        database.update(message.server, message.author, ['status'], ['Active'])
        await client.send_message(message.channel, 'You have now joined the Games!\n'
                                                   'Player: %(player)s\n'
                                                   'Money:  %(money)s\n\n'
                                                   'More information will follow as Games grow'
                                                    % {'player': user['Name'], 'money': user['Balance']})