import sqlite3 
import random
import re as regex

# Creates a connection to the database
def getDb():
    try:
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()
        query = "select sqlite_version();"
        cursor.execute(query)
        record = cursor.fetchall()
        print("SQLite Database Version is: ", record)
        cursor.close()
        return connection
    except sqlite3.Error as error:
        print("Error while connecting to sqlite database: ", error)

# Creates a table in the database if it doesn't exist
def createTable():
    try:
        database = getDb()
        create_table_query = """CREATE TABLE IF NOT EXISTS test (
                                id INTEGER PRIMARY KEY,
                                url TEXT NOT NULL,
                                short TEXT NOT NULL UNIQUE,
                                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                                );"""
        cursor = database.cursor()
        cursor.execute(create_table_query)
        database.commit()
        print("table create successfully")
        cursor.close()
        database.close()
    except sqlite3.Error as error:
        print("Error while connecting to the table: ", error)

# Selects 6 random characters from a string and returns it
def createRndStr():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    new = ""
    for i in range(6):
        new += random.choice(chars)
    return new

# Checks if the short URL has been used before
def hasBeenUsed(short : str):
    try:
        database = getDb()
        cursor = database.cursor()
        cursor.execute("""SELECT short FROM test WHERE short = ?;""", (short,))
        result = cursor.fetchone()
        print("short URL fetched successfully")
        cursor.close()
        database.close()
        if (result == None):
            return False
        else:
            return True
    except sqlite3.Error as error:
        print("Error while fetching short URL: ", error)

# Returns the URL that corresponds to the short URL
def getURL(short : str):
    try: 
        database = getDb()
        cursor = database.cursor()
        cursor.execute("""SELECT url FROM test WHERE short = ?;""", (short,))
        url = cursor.fetchone()
        print("short URL fetched successfully")
        cursor.close()
        database.close()
        print (url[0])
        return url
    except sqlite3.Error as error:
        print("Error while fetching short URL: ", error)

# Creates a new entry, inserts it into the database and returns the short URL
def createShort(url : str):
    try:
        database = getDb()
        cursor = database.cursor()
        short = createRndStr()
        while (hasBeenUsed(short)):
            short = createRndStr()
        tuple = (random.randint(1, 10000), url, short)
        cursor.execute("""INSERT INTO test
                       (id, url, short, created_at)
                        VALUES
                        (?, ?, ?, CURRENT_TIMESTAMP)
                        ;""", tuple)
        database.commit()
        print(f"short URL inserted successfully: {short}")
        cursor.close()
        database.close()
        return short
    except sqlite3.Error as error:
        print("Error while inserting short URL: ", error)

# Function that gets everything from the database (for debugging use only)
def getAll():
    try:
        database = getDb()
        cursor = database.cursor()
        cursor.execute("""SELECT * FROM test;""")
        all = cursor.fetchall()
        print("All fetched successfully")
        cursor.close()
        database.close()
        return all
    except sqlite3.Error as error:
        print("Error while fetching all: ", error)