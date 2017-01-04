import mysql.connector
from mysql.connector import errorcode
from config.auth import Db


def connect():
    try:
        global cnx
        global cursor
        cnx = mysql.connector.connect(**Db.config)
        cursor = cnx.cursor()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


def close():
    try:
        cnx.close()
        cursor.close()
    except NameError:
        print('No connection to close')


def new_server(server):
    table = (
        "CREATE TABLE `%(name)s` ("
        "  `user` varchar(30) NOT NULL,"
        "  `user_id` varchar(30) NOT NULL,"
        "  `balance` int(7) NOT NULL,"
        "  `loan` int(7) NOT NULL,"
        "  `winnings` int(7) NOT NULL,"
        "  `losses` int(7) NOT NULL,"
        "  `status` enum('Active','Inactive') NOT NULL"
        ") ENGINE=InnoDB" % {'name': server.name.replace(' ', '_')})

    add_member = ("INSERT INTO " + server.name.replace(' ', '_') + " "
                  "(user, user_id, balance, loan, winnings, losses, status) "
                  "VALUES (%(user)s, %(user_id)s, %(balance)s, %(loan)s, %(winnings)s, %(losses)s, %(status)s)")

    try:
        print("Creating table {}: ".format(server.name), end='')
        cursor.execute(table)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

    for member in server.members:
        data_member = {
            'user': member.name,
            'user_id': member.id,
            'balance': 500,
            'loan': 0,
            'winnings': 0,
            'losses': 0,
            'status': 'Inactive'
        }
        # print(data_member)
        cursor.execute(add_member, data_member)
        cnx.commit()


async def get(server, member):
    query = ("SELECT * FROM " + server.name.replace(' ', '_') + " WHERE user_id = " + str(member.id))

    try:
        cnx.reconnect()
        # close()
        # connect()
        cursor.execute(query)
    except mysql.connector.Error as err:
        print(err)

    row = cursor.fetchone()

    result = {'Name': row[0], 'User_id': row[1], 'Balance': row[2], 'Loan': row[3],
              'Winnings': row[4], 'Losses': row[5], 'Status': row[6]}

    return result


def update(server, member, items, values):

    update_set = ''
    for item, value in zip(items, values):
        if type(value) == int:
            update_set = update_set + ' ' + server.name.replace(' ', '_') + '.' + str(item) + ' = ' + str(value) + ','
        else:
            update_set = update_set + ' ' + server.name.replace(' ', '_') + '.`' + str(item) + '`' + ' = "' + str(value) + '",'
    update_set = update_set[:-1]

    query = ("UPDATE " + server.name.replace(' ', '_') + " SET" + update_set + " WHERE user_id = " + str(member.id))

    print(query)
    cursor.execute(query)
    cnx.commit()
