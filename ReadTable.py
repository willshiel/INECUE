import sqlite3
from Team import Team
conn = sqlite3.connect('databaseOfTeams.db')

c = conn.cursor()

c.execute('SELECT * FROM Teams')

team = Team()
team = c.fetchone()
#print team

c.close()
