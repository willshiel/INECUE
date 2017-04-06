# team object that has the name, points, assists, and rebounds
class Team:
    teamId = 0
    name = ''
    winningPercentage = 0.0
    PPG = 0.0
    APG = 0.0
    RPG = 0.0
    FGP = 0.0

    # getters and setters for team fields
    def setTeamId(self, teamId):
        self.teamId = teamId
    def getTeamId(self):
        return self.teamId
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setWinningPercentage(self, winningPercentage):
        self.winningPercentage = winningPercentage
    def getWinningPercentage(self):
        return self.winningPercentage
    def setPPG(self, PPG):
        self.PPG = PPG
    def getPPG(self):
        return self.PPG
    def setAPG(self, APG):
        self.APG = APG
    def getAPG(self):
        return self.APG
    def setRPG(self, RPG):
        self.RPG = RPG
    def getRPG(self):
        return self.RPG
    def setFGP(self, FGP):
        self.FGP = FGP
    def getFGP(self):
        return self.FGP

    # to string for visual representation
    def __str__(self):
        return "Id: " + str(self.teamId) + "\nName: " + self.name + "\nPPG: " + str(self.PPG) + "\nAPG: " + str(self.APG) + "\nRPG: " + str(self.RPG) + "\nFGP: " + str(self.FGP)
