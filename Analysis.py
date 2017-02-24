import sqlite3
from Team import Team

def main():
    conn = sqlite3.connect('databaseOfTeams.db')

    c = conn.cursor()

    c.execute('SELECT * FROM Teams')

    # fetches team from the database
    databaseTeam = c.fetchall()

    # close database access
    c.close()

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


def createHomeTeam(dbTeam):
    # Assign home team to object
    homeTeam = Team()
    homeTeam.setTeamId(dbTeam[0][0])
    homeTeam.setName(dbTeam[0][1])
    homeTeam.setPPG(dbTeam[0][2])
    homeTeam.setRPG(dbTeam[0][3])
    homeTeam.setAPG(dbTeam[0][4])
    return homeTeam

def createAwayTeam(dbTeam):
    # Assign away team to object
    awayTeam = Team()
    awayTeam.setTeamId(dbTeam[1][0])
    awayTeam.setName(dbTeam[1][1])
    awayTeam.setPPG(dbTeam[1][2])
    awayTeam.setRPG(dbTeam[1][3])
    awayTeam.setAPG(dbTeam[1][4])
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

main()
