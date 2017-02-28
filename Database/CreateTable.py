import sqlite3
conn = sqlite3.connect('DatabaseOfTeams.db')

c = conn.cursor()

# creates initial table for all of the teams
c.execute('''CREATE TABLE Results
                            (id INTEGER PRIMARY KEY, HomeTeam TEXT, AwayTeam TEXT, Spread REAL, Result TEXT)''')



conn.commit()
conn.close()
