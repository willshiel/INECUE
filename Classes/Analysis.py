import sqlite3
from Team import Team

def main():
    conn = sqlite3.connect('../Database/databaseOfTeams.db')

    c = conn.cursor()

    c.execute('SELECT * FROM Teams')

    # fetches team from the database
    databaseTeam = c.fetchall()

    # creates the team objects
    t1 = createHomeTeam(databaseTeam)
    t2 = createAwayTeam(databaseTeam)

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
        print t2.getName()
        print abs(spread)

    writeToDatabase(t1.getName(), t2.getName(), spread, c)

    conn.commit()
    conn.close()


def createHomeTeam(dbTeam):
    # Assign home team to object
    homeTeam = Team()
    homeTeam.setTeamId(dbTeam[12][0])
    homeTeam.setName(dbTeam[12][1])
    homeTeam.setPPG(dbTeam[12][2])
    homeTeam.setRPG(dbTeam[12][3])
    homeTeam.setAPG(dbTeam[12][4])
    return homeTeam

def createAwayTeam(dbTeam):
    # Assign away team to object
    awayTeam = Team()
    awayTeam.setTeamId(dbTeam[13][0])
    awayTeam.setName(dbTeam[13][1])
    awayTeam.setPPG(dbTeam[13][2])
    awayTeam.setRPG(dbTeam[13][3])
    awayTeam.setAPG(dbTeam[13][4])
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
    noResult = 'No Result Yet'
    cursor.execute('''INSERT INTO Results VALUES(?, ?, ?, ?, ?)''',(1, homeTeam, awayTeam, spread, noResult))

main()
