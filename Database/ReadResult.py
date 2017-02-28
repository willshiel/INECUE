import sqlite3
conn = sqlite3.connect('DatabaseOfTeams.db')

c = conn.cursor()

# query for all teams in the db
query = "SELECT * FROM Results"

c.execute(query)

# print the list of teams
teams = c.fetchall()

print teams

conn.close()
