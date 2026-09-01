import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="",
    database="python_421_python"
)

mycursor = mydb.cursor()


sql = """
CREATE TABLE customers (
    name VARCHAR(255),
    address VARCHAR(255))
"""


mycursor.execute(sql)
