import discord
import random

async def roll(client, message, *args):
    min = 1
    max = 6
    dice = random.randint(min, max)
    file = '../img/dice/dice' + str(dice) + '.png'

    await client.send_file(message.channel, file)
