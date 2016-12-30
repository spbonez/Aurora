import random
Helper = {
    '!roll':{'Help':'!roll', 'Description':'Rolls the Dice', 'Type':'User'}
}
async def roll(client, message, *args):
    min = 1
    max = 6
    dice = random.randint(min, max)
    file = '../img/dice/dice' + str(dice) + '.png'

    if str(message.author.id) == '119170394820182018':
        file = '../img/dice/dice6.png'
    await client.send_file(message.channel, file)
