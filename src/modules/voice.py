import discord

if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')


async def vjoin(client, message, args):
    print(args)
    channel = discord.utils.get(message.server.channels, name="🎶 Music Test", type=discord.ChannelType.voice)

    try:
        await client.join_voice_channel(channel)
    except discord.InvalidArgument:
        print('This is not a voice channel...')
    except discord.ClientException as e:
        print('Already in a voice channel...', e)
    else:
        print('Ready to play audio in ')
        player = await discord.voice.create_ytdl_player('https://www.youtube.com/watch?v=d62TYemN6MQ')
        player.start()

async def vleave(client, message, args):
    await client.disconnect()
