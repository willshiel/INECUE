from bs4 import BeautifulSoup
import urllib2
import re

# list of players ids within the espn website
urlList = [('tj-mcconnell', '2530530'), ('nerlens-noel', '2991280'), ('robert-covington', '2490620'), ('jahlil-okafor', '3135048'), ('ersan-ilyasova', '2767')]

# Philadelphia 76ers Roster
Philadelphia = {}

playerIndex = 0
for player in urlList:
    # open the html as a file
    response = urllib2.urlopen('http://www.espn.com/nba/player/_/id/' + urlList[playerIndex][1] + "/" + urlList[playerIndex][1] )
    html = response.read()

    # initialize BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    # find the name of the player
    nameHTML = soup.findAll('h1')
    name = re.search('[A-Z](.*)[a-z]\<', str(nameHTML)).group(0)
    name = name[:-1]
    print name

    positionList = soup.find('ul', {'class', 'general-info'})
    positionLine = positionList.findChildren('li')
    # if regex doesn't match then position is Center
    # currently does not work correctly
    position = re.search('[A-Z]([A-Z]\<)', str(positionLine)).group(0)
    if position is not 'C':
        position = position[1:-1]

    # find the header stats for each player
    header = soup.find('table', {'class', 'header-stats'})
    seasonStats = header.findChildren('tr')

    statMap = {}
    # append the stats to a list
    count = 0
    for stat in seasonStats[0]:
        stat = str(stat)
        numberStat = re.search('\d(.*)\d', stat).group()
        if count % 4 is 0:
            statMap['PPG'] = numberStat
        elif count % 4 is 1:
            if position is 'G':
                statMap['APG'] = numberStat
            else:
                statMap['RPG'] = numberStat
        elif count % 4 is 2:
            if position is 'G':
                statMap['RPG'] = numberStat
            else:
                statMap['BPG'] = numberStat
        elif count % 4 is 3:
            statMap['PER'] = numberStat
        count += 1

    Philadelphia[name] = statMap
    playerIndex += 1

print Philadelphia
