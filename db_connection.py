import pymysql

def connect_db():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='12345678',
        database='nutrition_db'
    )
    cursor = connection.cursor()
    return connection, cursor
