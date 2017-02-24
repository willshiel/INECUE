import sqlite3
conn = sqlite3.connect('DatabaseOfTeams.db')

c = conn.cursor()

# Drops all teams from the database
query = 'DELETE FROM Teams where id < 30'

c.execute(query)

conn.commit()
conn.close()
