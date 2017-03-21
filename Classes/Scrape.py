# import modules
from bs4 import BeautifulSoup
import urllib2
import re
import sqlite3
from Team import Team

# list of all nba team ids on espn
NBA = ['phi', 'ny', 'atl', 'bos', 'bkn', 'cha', 'chi', 'cle', 'dal', 'den', 'det', 'gsw', 'hou', 'ind', 'lac', 'lal', 'mem', 'mia', 'mil']
NBA.extend(['min', 'no', 'okc', 'orl', 'pho', 'por', 'sac', 'sas', 'tor', 'utah', 'was'])

def main():
    teamId = 0
    for team in NBA:
        print team
        response = urllib2.urlopen('http://www.espn.com/nba/team/stats/_/name/' + team)
        html = response.read()

        # initialize BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        team = Team()

        # set unique Id then increment for the following team's Id
        scrapeID(team, teamId)
        teamId += 1

        # scrape all data from espn and place into team object
        scrapeName(team, soup)
        scrapeStats(team, soup)

        # write to a database
        conn = sqlite3.connect('../Database/databaseofTeams.db')
        c = conn.cursor()

        writeTeam(team, c)

        conn.commit()
        conn.close()

        print team

# parse for information and apply it to object fields
def scrapeID(t, teamId):
    t.setTeamId(teamId)

def scrapeName(t, soup):
    # scrape name and trime html tags
    name = str(soup.find('b'))
    name = name[3:-4]
    t.setName(name)

# gets the ppg, rpg, and apg and sets to objects
def scrapeStats(t, soup):
    # get main data table
    table = soup.find('table')
    rows = str(table.findAll('tr', attrs={'class':'total'}))
    # get the totals row from the table
    rows = rows.split('</td>')
    # set the fields in the object
    for row in range(0, len(rows)):
        # if a row is ppg, rpg, or apg
        if row is 4:
            rows[row] = rows[row][18:]
            t.setPPG(float(rows[row]))
        if row is 7:
            rows[row] = rows[row][18:]
            t.setRPG(float(rows[row]))
        if row is 8:
            rows[row] = rows[row][18:]
            t.setAPG(float(rows[row]))

def writeTeam(t, cursor):
    teamId = t.getTeamId()
    name = t.getName()
    PPG = t.getPPG()
    RPG = t.getRPG()
    APG = t.getAPG()
    # insert row of data
    cursor.execute('''INSERT INTO Teams
                                VALUES(?, ?, ?, ?, ?)''',(teamId, name, PPG, RPG, APG))

main()
