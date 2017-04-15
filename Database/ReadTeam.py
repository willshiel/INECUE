import sqlite3
conn = sqlite3.connect('DatabaseOfTeams.db')

c = conn.cursor()

c.execute("""SELECT * FROM Teams""")
team = c.fetchall()
print team

conn.close()
