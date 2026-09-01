import sqlite3

conn = sqlite3.connect("./atm.db")
c = conn.cursor()

c.execute(
    """CREATE TABLE IF NOT EXISTS users 
             (card_number TEXT PRIMARY KEY, national_code TEXT, name TEXT, pin TEXT, balance REAL)"""
)

conn.commit()

sql = """
insert into users values (?, ?, ?, ?, ?)
"""
c.execute(sql, ("123", "098765", "ali", "1234", "500"))

conn.commit()

conn.close()