import sqlite3

connection = sqlite3.connect("./mydb.db")
cursor = connection.cursor()
sql = """
 CREATE TABLE IF NOT EXISTS user (
 userId INTEGER ,
 name VARCHAR (60),
 family VARCHAR (60),
 email VARCHAR (60)
 );
"""
cursor.execute(sql)
connection.commit()
connection.close()
