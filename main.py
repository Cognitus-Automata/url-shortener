import sqlite3 
import random
from flask import Flask, render_template

# Function that creates a connection to the database
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
        print("Error while connecting to sqlite database", error)

# Function that closes the connection to the database
# def closeDb():
#     try:
#         connection = getDb()
#         connection.close()
#         print("The SQLite connection is closed")
#     except sqlite3.Error as error:
#         print("Error while closing the connection", error)
    
# Function that creates a table in the database
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
        print("Error while connecting to the table", error)

# Function that creates a short URL (6 characters)
def createRndStr():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    new = ""
    for i in range(6):
        new += random.choice(chars)
    return new

# Function that gets the Full URL from the database
def getURL(short):
    try: 
        database = getDb()
        cursor = database.cursor()
        cursor.execute("""SELECT url FROM test WHERE short = ?;""", (short,))
        url = cursor.fetchone()
        print("short URL fetched successfully")
        cursor.close()
        database.close()
        return url
    except sqlite3.Error as error:
        print("Error while fetching short URL", error)

# Function that creates a new entry, inserts it into the database and returns the short URL
def createShort(url):
    try:
        database = getDb()
        cursor = database.cursor()
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
        print("Error while inserting short URL", error)

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
        print("Error while fetching all", error)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/rnd')
def rnd():
    return f"Your short URL is {createShort('https://www.google.com')}"

if __name__ == "__main__":
    createTable()

    app.run(debug=True)


    

