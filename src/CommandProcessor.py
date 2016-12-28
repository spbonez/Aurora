import src.modules as module
import src.permission as perm


def begin(client):

    for cmd in module.__all__:
        print(cmd)

    @client.event
    async def on_message(message):
        if message.author != client.user:
            print('New message from:', message.author, 'in Channel:', message.channel, '\nContent:', message.content)

        if message.content.startswith('!'):
            if await perm.have_permission(message.author):
                msg = message.content.lower().split(' ')
                command = msg[0]
                command = command.replace('!', '')
                del msg[0]
                argument = ' '.join(msg)
                try:
                    await getattr(module, command)(client, message, argument)
                except AttributeError and TypeError:
                    await client.send_message(message.channel, 'Sry that is not a command,'
                                                               ' did you spell it right ?')
            else:
                await client.send_message(message.channel, 'Im sry, but you dont have permission to use commands')
