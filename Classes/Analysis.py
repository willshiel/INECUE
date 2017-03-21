import sqlite3
from Team import Team

primaryID = 2

def main():
    conn = sqlite3.connect('../Database/databaseOfTeams.db')

    c = conn.cursor()

    # date for file writing and reading
    date = '3162017'

    # reads matchups from file
    fileRead = open('Games/{0}.txt'.format(date), 'r').readlines()
    storedMatchups = fileRead[0].split('|')
    for item in storedMatchups:
        if item is '':
            break
        # get the hometeam vs the awayteam
        matchup = item.split('^')
        # split the stats into a tuple
        homeTeamList = matchup[0].split(',')
        awayTeamList = matchup[1].split(',')
        # assign each team's id to a variable
        homeTeamId = homeTeamList[0][1:]
        awayTeamId = awayTeamList[0][1:]

        c.execute('SELECT * FROM Teams WHERE id = {0}'.format(homeTeamId))

        # fetches team from the database
        databaseTeam = c.fetchall()
        # creates the team objects using the teams id
        t1 = createHomeTeam(databaseTeam[0][0], databaseTeam)

        c.execute('SELECT * FROM Teams WHERE id = {0}'.format(awayTeamId))
        # gets team from database
        databaseTeam = c.fetchall()

        t2 = createAwayTeam(databaseTeam[0][0], databaseTeam)

        # initializes the spread
        spread = 0.0

        # finds the disparity in PPG and assigns to spread
        spread = getPoints(t1, t2)

        # apply rebound and assist advantage
        spread += getRebounds(t1, t2)
        spread += getAssists(t1, t2)

        # apply home court advantage
        spread += 3.0
        # find the team that has the better score
        if spread < 0:
            print "{0} is the winner and the spread is {1}".format(t2.getName(), abs(spread))
        else:
            print "{0} is the winner and the spread is {1}".format(t1.getName(), abs(spread))

        writeToDatabase(t1.getName(), t2.getName(), spread, c)

    conn.commit()
    conn.close()


def createHomeTeam(idNum, dbTeam):
    # Assign home team to object
    homeTeam = Team()
    homeTeam.setTeamId(dbTeam[0][0])
    homeTeam.setName(dbTeam[0][1])
    homeTeam.setPPG(dbTeam[0][2])
    homeTeam.setRPG(dbTeam[0][3])
    homeTeam.setAPG(dbTeam[0][4])
    return homeTeam

def createAwayTeam(idNum, dbTeam):
    # Assign away team to object
    awayTeam = Team()
    awayTeam.setTeamId(dbTeam[0][0])
    awayTeam.setName(dbTeam[0][1])
    awayTeam.setPPG(dbTeam[0][2])
    awayTeam.setRPG(dbTeam[0][3])
    awayTeam.setAPG(dbTeam[0][4])
    return awayTeam

# gets the disparity in PPG
def getPoints(t1, t2):
    return t1.getPPG() - t2.getPPG()

# gets the disparity in rebounds
def getRebounds(t1, t2):
    if t1.getRPG() > t2.getRPG():
        return 2.0
    else:
        return -2.0

# gets the disparity in assists
def getAssists(t1, t2):
    if t1.getAPG() > t2.getAPG():
        return 2.0
    else:
        return -2.0

def writeToDatabase(homeTeam, awayTeam, spread, cursor):
    global primaryID
    noResult = 'No Result Yet'
    #cursor.execute('''INSERT INTO Results VALUES(?, ?, ?, ?, ?)''',(primaryID, homeTeam, awayTeam, spread, noResult))
    primaryID += 1

main()
