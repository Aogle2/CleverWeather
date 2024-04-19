from mysql import connector as cn



def DBConnect():
    connection = cn.connect(user ="aogle", password = "local#123", host="raspberrypi",database='information_schema')
    print(connection.get_server_info())
    cur = connection.cursor()
    querey = "show tables;"
    cur.execute(querey)
    for row in cur.fetchall():
        #print(row[0])
        for table in row:
            new  = connection.cursor()
            newq = f"select * from {table};"
            new.execute(newq)
            for newstuff in new.fetchall():
                print(newstuff)

    cur.close()
    connection.close()


DBConnect()
