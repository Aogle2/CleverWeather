from mysql import connector as cn



def DBConnect():
    connection = cn.connect(user ="aogle", password = "local#123", host="raspberrypi")
    print(connection.get_server_info())
    connection.close()


DBConnect()
