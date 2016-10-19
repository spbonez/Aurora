import os
async def list(client, message, *args):
        modules = os.listdir('.\modules')

        modules.remove('__init__.py')
        modules.remove('__pycache__')
        command = []
        print(modules)
        for module in modules:
            mymodule = module.replace('.py','')
            cmd = '!' + mymodule
            command.append(cmd)
        mycommand = str(command)
        mycommand = mycommand.replace('[','')
        mycommand = mycommand.replace(']', '')
        mycommand = mycommand.replace("'", "")
        mycommands = mycommand.replace(', ', '\n')

        await client.send_message(message.channel, '```' + mycommands + '```')