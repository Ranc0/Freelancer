import mysql.connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'asdasd'
)
cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE db")
print("all done")