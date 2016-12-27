import discord.utils as utils

Bot_Name = 'FlixBot'
Admin_Name = 'Flixbot Admin.'
Muted = 'Muted'
Everyone = '@everyone'

async def have_permission(user):
    if utils.get(user.roles, name=Admin_Name) is not None:
        return 2
    elif utils.get(user.roles, name=Muted) is not None:
        return 0
    elif utils.get(user.roles, name=Everyone) is not None:
        return 1
