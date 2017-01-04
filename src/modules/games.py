import src.Database as database
import random
Helper = {
    '!join_games': {'Help': '!join_games', 'Description': 'Jump in the wonderful world of Games,'
                                                          ' and get your starting bonus of 500 bucks!!!\n'
                                                          'This is the sure way to get yourself the biggest'
                                                          'Gambling Addiction in the world!!\n'
                                                          'So suit up! empty that piggy bank of yours,'
                                                          'and start gambling!!', 'Type': 'Game'},
    '!chance': {'Help': '!chance or !bet [Amount] [Odds]', 'Description': 'Gamble you money with no security'
                                                                          ' what so ever\nthe higher odds you'
                                                                          ' take, the bigger your reward will be',
                                                           'Type': 'Game'},
    '!bet': {'Help': '!chance or !bet [Amount] [Odds]', 'Description': 'Gamble you money with no security'
                                                                       ' what so ever\nthe higher odds you'
                                                                       ' take, the bigger your reward will be',
                                                         'Type': 'Game'},
    '!spin': {'Help': '!spin [number of spins]x[money to throw on each spin]', 'Description': 'Spin the wheal of '
                                                                                'furtune, try your luck. agian, the'
                                                                                ' the more you risk, the higher payday.'
                                                                                ,'Type': 'Game'}
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

async def dice_game(client, message, arg):
    await client.send_message(message.channel, 'Dice game is not Available yet')


async def chance(client, message, arg):
    player = await database.get(message.server, message.author)
    flag = 1
    odds = None
    bet = None

    if player['Status'] == 'Active':
        await client.send_message(message.channel,
                                        '```'
                                        '  Odds  | Winnings\n'
                                        '  1:5   |   500%  \n'
                                        '  1:10  |  1000%  \n'
                                        '  1:20  |  2000%  \n'
                                        '  1:50  |  5000%  \n'
                                        'To start, type #bet [Amount] [Odds]'
                                        '```')

        def check(msg):
            if msg.content.startswith('#bet'):
                args = msg.content[5:].split(' ')
                nonlocal odds, bet
                odds = args[1]
                bet = args[0]
                return True
            else:
                return False

        msg = await client.wait_for_message(timeout=60, author=message.author, channel=message.channel, check=check)
        while msg is not None:
            while int(bet) > int(player['Balance']):
                await client.send_message(message.channel, 'You do not have enough money to place that bet.\n'
                                                           'Place a new bet using #bet.\n'
                                                           'Your current balance: %(balance)s'
                                                            % {'balance': player['Balance']})
                msg = await client.wait_for_message(timeout=10, author=message.author, channel=message.channel,
                                                    check=check)
                if msg is None:
                    break
            else:
                try:
                    await make_bet(client, message, player, odds, bet)
                    msg = None
                    flag = 0
                except ValueError:
                    await client.send_message(message.channel, "There was an error in your request,\n"
                                                               "Try again using #bet")
                    msg = await client.wait_for_message(timeout=10, author=message.author, channel=message.channel,
                                                        check=check)
                    if msg is None:
                        break
        else:
            if flag:
                await client.send_message(message.channel, 'Bet canceled! (Timeout)')
    else:
        await client.send_message(message.channel, 'You need to Activate games firs, see !help !join_games for info')


async def bet(client, message, arg):
    player = await database.get(message.server, message.author)
    amount = None
    odds = None
    msg = None
    flag = 0


    def check(msg):
        if msg.content.startswith('#bet'):
            args = msg.content[5:].split(' ')
            nonlocal odds, amount
            odds = args[1]
            amount = args[0]
            return True
        else:
            return False

    if player['Status'] == 'Active':
        arg = arg.split(' ')
        amount = arg[0]
        odds = arg[1]

        while int(amount) > int(player['Balance']):
            await client.send_message(message.channel, 'You do not have enough money to place that bet.\n'
                                                       'Place a new bet using #bet.\n'
                                                       'Your current balance: %(balance)s'
                                      % {'balance': player['Balance']})
            msg = await client.wait_for_message(timeout=10, author=message.author, channel=message.channel,
                                                check=check)
            if msg is None:
                flag = 1
                break
        else:
            try:
                await make_bet(client, message, player, odds, amount)
            except ValueError:
                await client.send_message(message.channel, "There was an error in your request!")
    if flag:
        await client.send_message(message.channel, 'Bet canceled! (Timeout)')


async def make_bet(client, message, player, odds, amount):
    await client.send_message(message.channel, 'Betting %(bet)s on odds %(odds)s'
                              % {'bet': amount, 'odds': odds})

    odds = odds.split(':')
    number = random.randint(int(odds[0]), int(odds[1]))

    if number is 1:
        winnings = int(((int(amount) / 100) * (int(odds[1]) * 100))-int(amount))
        await client.send_message(message.channel, 'Victory ! Winnings: %(win)s'
                                  % {'win': winnings})
        database.update(message.server, message.author, {'balance'},
                        {int(winnings + int(player['Balance']))-int(amount)})
    else:
        await client.send_message(message.channel, 'Ouch, that just cost you %(los)s bucks!'
                                  % {'los': int(amount)})
        database.update(message.server, message.author, {'balance'},
                        {int(int(player['Balance'])) - int(amount)})


class Prize:
    prizes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
              10, 10, 10, 10,
              100]

    total_prizes = len(prizes)

async def spin(client, message, arg):
    player = await database.get(message.server, message.author)
    if player['Status'] == 'Active':
        arg = arg.split('x')
        args = []
        for v in arg:
            if v.startswith(' '):
                args.append(v[1:])
            else:
                args.append(v)
        spins = args[0]
        value = args[1]

        if int(spins) > 10:
            await client.send_message(message.channel, 'There is a maximum of 10 spins!')
            return

        if int(value) > 5000:
            await client.send_message(message.channel, 'Highest bet allowed is 5000!')
            return

        price = int(value) * int(spins)

        prizes = Prize.prizes

        if int(price) <= int(player['Balance']):

            msg = ('Total winnings over {:^3} spins: {:^3}\n'
                   'Rounds: ```\n')
            total_winnings = 0
            for i in range(int(spins)):
                number = random.randint(1, len(prizes)-1)
                win = int(value) * int(prizes[number])
                total_winnings += win
                msg += ('Round: {:^3}  Result: x{:^3}   Win: {} \n'.format(i+1, prizes[number], win))

            msg += '```'
            print(total_winnings - price)
            await client.send_message(message.channel, msg.format(spins, total_winnings - price))

            database.update(message.server, message.author, {'balance'},
                            {int(total_winnings + int(player['Balance']))-int(price)})
        else:
            await client.send_message(message.channel, 'You do not have enough money to place that spin.\n'
                                                       'Your current balance: %(balance)s \n'
                                                       'This spin will cost %(cost)s'
                                      % {'balance': player['Balance'], 'cost': price})
    else:
        await client.send_message(message.channel, 'You need to Activate games firs, see !help !join_games for info')


async def spin_chances(client, message, arg):

    prizes = Prize.prizes
    total_prizes = Prize.total_prizes

    chances = {
        'chance_of_0': (len([i for i, x in enumerate(prizes) if x == 0]) / total_prizes)*100,
        'chance_of_1': (len([i for i, x in enumerate(prizes) if x == 1]) / total_prizes)*100,
        'chance_of_2': (len([i for i, x in enumerate(prizes) if x == 2]) / total_prizes)*100,
        'chance_of_5': (len([i for i, x in enumerate(prizes) if x == 5]) / total_prizes)*100,
        'chance_of_10': (len([i for i, x in enumerate(prizes) if x == 10]) / total_prizes)*100,
        'chance_of_100': (len([i for i, x in enumerate(prizes) if x == 100]) / total_prizes)*100
    }

    msg = '**{}**' \
          '```' \
          '{:.20}\n' \
          '{:.20}\n' \
          '{:.20}\n' \
          '{:.20}\n' \
          '{:.20}\n' \
          '{:.20}\n' \
          '```'.format('Spin Chances',
                       'Chance of x0: ' + str(chances['chance_of_0']),
                       'Chance of x1: ' + str(chances['chance_of_1']),
                       'Chance of x2: ' + str(chances['chance_of_2']),
                       'Chance of x5: ' + str(chances['chance_of_5']),
                       'Chance of x10: ' + str(chances['chance_of_10']),
                       'Chance of x100: ' + str(chances['chance_of_100']))

    await client.send_message(message.channel, msg)

async def account(client, message, arg):
    player = await database.get(message.server, message.author)

    await client.send_message(message.channel, 'Account details: \n'
                                               '```'
                                               'User: {}\n'
                                               'Balance: {}'
                                               '```'.format(player['Name'], player['Balance']))