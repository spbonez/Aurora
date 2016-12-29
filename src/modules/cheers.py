import random
import os
Helper = {
    '!cheers':{'Help':'!cheers', 'Description':'cheers mate!', 'Type':'User'}
}
async def cheers(client, message, *args):
    beers = os.listdir('../img/beers')
    min = 1
    max = len(beers)
    number = random.randint(min, max)
    file = '../img/beers/beer' + str(number) + '.jpg'

    await client.send_file(message.channel, file)
