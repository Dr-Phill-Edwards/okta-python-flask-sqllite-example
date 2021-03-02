import sqlite3

connection = sqlite3.connect('message.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE messages(id INTEGER PRIMARY KEY AUTOINCREMENT, message TEXT)''')
cursor.execute("INSERT INTO messages (message) VALUES('Welcome')")
connection.commit()

cursor.execute('SELECT id, message FROM messages ORDER BY id')
for row in cursor:
    print(row)

connection.close()
