import sqlite3
conn = sqlite3.connect('DatabaseOfTeams.db')

c = conn.cursor()
date = '2272017'

openFile = open('Games/{0}.txt'.format(date), 'r')
myFile = openFile.readlines()

# data structure to store matchups for future file writing
storedMatchups = []

# read teams from text file
splitMatchup = myFile[0].split('|')
for matchup in range(0, len(splitMatchup) - 1):
    # loop through the list of matchups
    splitTeams = splitMatchup[matchup].split(',')
    homeTeam = splitTeams[1]
    awayTeam = splitTeams[0]

    # find the teams that are being matched up against each other
    query = "SELECT * FROM Teams WHERE Name = '{0}' UNION ALL SELECT * FROM Teams WHERE Name = '{1}'".format(homeTeam, awayTeam)

    c.execute(query)

    teams = c.fetchall()

    # appends matchup to list
    storedMatchups.append(teams)

# opens file to write matchups to
writeFile = open('../Classes/Games/{0}.txt'.format(date), 'w+')
# writes to the file
for item in storedMatchups:
    writeFile.write('{0},{1}|'.format(item[0], item[1]))

conn.close()
