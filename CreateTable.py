import sqlite3
conn = sqlite3.connect('DatabaseOfTeams.db')

c = conn.cursor()

# creates initial table for all of the teams
c.execute('''CREATE TABLE Teams
                            (id INTEGER, Name TEXT, PPG REAL, APG REAL, RPG REAL)''')

# insert row of data
#c.execute('''INSERT INTO players
#                            VALUES(0, 'TJ McConnell', 6.3, 6.1, 3.0)''')

conn.commit()
conn.close()
