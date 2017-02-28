import sqlite3
conn = sqlite3.connect('DatabaseOfTeams.db')

c = conn.cursor()

write = """UPDATE Results
           SET Result = 'Loss'
           WHERE id = 0"""

c.execute(write)

conn.commit()
conn.close()
