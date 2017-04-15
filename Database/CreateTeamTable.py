import sqlite3
conn = sqlite3.connect('DatabaseOfTeams.db')

c = conn.cursor()

c.execute('''DROP TABLE if exists Teams''')

# creates initial table for all of the teams
c.execute('''CREATE TABLE Teams
                            (id INTEGER PRIMARY KEY, Name TEXT, PPG REAL, RPG REAL, APG REAL, FGP REAL)''')



conn.commit()
conn.close()
