class Roles:
    class Admin:
        Name = 'Founder'
        ID = '228212690424692736'
        Level = 3

    class Member:
        Name = 'Member'
        ID = '228213036475875328'
        Level = 2

    class Everyone:
        Name = '@everyone'
        ID = '228212523885658112'
        Level = 1

    class Muted:
        Name = 'Muted'
        ID = '235904268098338816'
        Level = 0


async def have_access(member):
    levels = []
    for role in member.roles:
        if role.id == Roles.Admin.ID:
            levels.append(Roles.Admin.Level)
        elif role.id == Roles.Member.ID:
            levels.append(Roles.Member.Level)
        elif role.id == Roles.Everyone.ID:
            levels.append(Roles.Everyone.Level)
        elif role.id == Roles.Muted.ID:
            return 0
    return max(levels)


async def update(client):
    for server in client.servers:
        print(server)
        for roles in server.roles:
            print(roles.name + '|' + roles.id)
