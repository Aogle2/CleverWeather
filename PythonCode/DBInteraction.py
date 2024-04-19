from mysql import connector as cn



def DBConnect():
    connection = cn.connect(user ="aogle", password = "local#123", host="raspberrypi",database='mysql')
    print(connection.get_server_info())
    cur = connection.cursor()
    querey = "SELECT * FROM user;"
    cur.execute(querey)
    for row in cur.fetchall():
        print(row)
        print(row[0])

    connection.close()


DBConnect()
