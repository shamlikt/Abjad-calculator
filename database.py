import sqlite3

db = sqlite3.connect('data')
cu = db.cursor()
cu.execute('''CREATE TABLE abjid(id INTIGER PRIMARY KEY,letter TEXT,
            value INTIGER)''')
db.commit()

