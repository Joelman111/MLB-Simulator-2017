import pygame

def readFile(path):
    with open(path, 'r') as f:
        return f.read()

def writeFile(path, contents):
    with open(path, 'w') as f:
        f.write(contents)

def changeFile(path, contents):
    with open(path, 'a') as f:
        f.write(contents)

def getRoster(name):
    roster=readFile('assets\\teamData\\rosters\\%s.txt'%name)
    names=[]
    for line in roster.splitlines():
        names.append(line)
    return names

class Team(object):
    def __init__(self,abbrev,players):
        #print(abbrev)
        self.abbrev=abbrev
        rostNames=getRoster(self.abbrev)
        self.roster=self.createRoster(rostNames,players)
        self.fielders=self.getFielders(self.roster)
        self.pitchers=self.getPitchers(self.roster)
        self.normLineup,self.dhLineup=self.getLineup(abbrev,self.roster)
        self.rotation=self.getRotation(abbrev,self.roster)
        self.relievers=self.getRelievers(self.pitchers,self.rotation)
        self.normBench=self.getBench(self.fielders,self.normLineup)
        self.dhBench=self.getBench(self.fielders,self.dhLineup)
        #print(self.normLineup)
        if abbrev=='ARZ':
            self.fullName='Arizona Dimondbacks'
            self.city='Phoenix, AZ'
            self.cityName='Arizona'
            self.name='Dimondbacks'
            self.logo=pygame.image.load('assets\\logos\\ARZ_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(167,25,48),(0,0,0)]
        elif abbrev=='ATL':
            self.fullName='Atlanta Braves'
            self.city='Atlanta, GA'
            self.cityName='Atlanta'
            self.name='Braves'
            self.logo=pygame.image.load('assets\\logos\\ATL_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(19,39,79),(255,255,255)]
        elif abbrev=='BAL':
            self.fullName='Baltimore Orioles'
            self.city='Baltimore, MD'
            self.cityName='Baltimore'
            self.name='Orioles'
            self.logo=pygame.image.load('assets\\logos\\BAL_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(223,70,1),(0,0,0)]
        elif abbrev=='BOS':
            self.fullName='Boston Red Sox'
            self.city='Boston, MA'
            self.cityName='Boston'
            self.name='Red Sox'
            self.logo=pygame.image.load('assets\\logos\\BOS_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(13,43,86),(189,48,57)]
        elif abbrev=='CHC':
            self.fullName='Chicago Cubs'
            self.city='Chicago, IL'
            self.cityName='Chicago'
            self.name='Cubs'
            self.logo=pygame.image.load('assets\\logos\\CHC_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(14,51,134),(204,52,51)]
        elif abbrev=='CHW':
            self.fullName='Chicago White Sox'
            self.city='Chicago, IL'
            self.cityName='Chicago'
            self.name='White Sox'
            self.logo=pygame.image.load('assets\\logos\\CHW_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(0,0,0),(196,206,212)]
        elif abbrev=='CIN':
            self.fullName='Cincinnati Reds'
            self.city='Cincinnati, OH'
            self.cityName='Cincinnati'
            self.name='Reds'
            self.logo=pygame.image.load('assets\\logos\\CIN_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(198,1,31),(255,255,255)]
        elif abbrev=='CLE':
            self.fullName='Cleveland Indians'
            self.city='Cleveland, OH'
            self.cityName='Cleveland'
            self.name='Indians'
            self.logo=pygame.image.load('assets\\logos\\CLE_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(0,43,92),(227,25,55)]
        elif abbrev=='COL':
            self.fullName='Colorado Rockies'
            self.city='Denver, CO'
            self.cityName='Colorado'
            self.name='Rockies'
            self.logo=pygame.image.load('assets\\logos\\COL_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(35,31,32),(61,61,112)]
        elif abbrev=='DET':
            self.fullName='Detroit Tigers'
            self.city='Detroit, MI'
            self.cityName='Detroit'
            self.name='Tigers'
            self.logo=pygame.image.load('assets\\logos\\DET_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(12,44,86),(255,255,255)]
        elif abbrev=='HOU':
            self.fullName='Houston Astros'
            self.city='Houston, TX'
            self.cityName='Houston'
            self.name='Astros'
            self.logo=pygame.image.load('assets\\logos\\HOU_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(0,45,98),(235,110,31)]
        elif abbrev=='KC':
            self.fullName='Kansas City Royals'
            self.city='Kansas City, MO'
            self.cityName='Kansas City'
            self.name='Royals'
            self.logo=pygame.image.load('assets\\logos\\KC_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(0,70,135),(192,154,91)]
        elif abbrev=='LAA':
            self.fullName='Los Angeles Angels'
            self.city='Anaheim, CA'
            self.cityName='Los Angeles'
            self.name='Angels'
            self.logo=pygame.image.load('assets\\logos\\LAA_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(186,0,33),(0,50,99)]
        elif abbrev=='LAD':
            self.fullName='Los Angeles Dodgers'
            self.city='Los Angeles, CA'
            self.cityName='Los Angeles'
            self.name='Dodgers'
            self.logo=pygame.image.load('assets\\logos\\LAD_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(0,90,156),(255,255,255)]
        elif abbrev=='MIA':
            self.fullName='Miami Marlins'
            self.city='Miami, FL'
            self.cityName='Miami'
            self.name='Marlins'
            self.logo=pygame.image.load('assets\\logos\\MIA_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(255,102,0),(0,0,0)]
        elif abbrev=='MIL':
            self.fullName='Milwaukee Brewers'
            self.city='Milwaukee, WI'
            self.cityName='Milwaukee'
            self.name='Brewers'
            self.logo=pygame.image.load('assets\\logos\\MIL_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(10,35,81),(182,146,46)]
        elif abbrev=='MIN':
            self.fullName='Minnesota Twins'
            self.city='Minneapolis, MN'
            self.cityName='Minnesota'
            self.name='Twins'
            self.logo=pygame.image.load('assets\\logos\\MIN_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(0,43,92),(211,17,69)]
        elif abbrev=='NYM':
            self.fullName='New York Mets'
            self.city='New York, NY'
            self.cityName='New York'
            self.name='Mets'
            self.logo=pygame.image.load('assets\\logos\\NYM_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(0,45,114),(255,89,16)]
        elif abbrev=='NYY':
            self.fullName='New York Yankees'
            self.city='New York, NY'
            self.cityName='New York'
            self.name='Yankees'
            self.logo=pygame.image.load('assets\\logos\\NYY_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(0,48,135),(255,255,255)]
        elif abbrev=='OAK':
            self.fullName='Oakland Athletics'
            self.city='Oakland, CA'
            self.cityName='Oakland'
            self.name='Athletics'
            self.logo=pygame.image.load('assets\\logos\\OAK_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(0,56,49),(239,178,30)]
        elif abbrev=='PHI':
            self.fullName='Philadelphia Phillies'
            self.city='Philadelphia, PA'
            self.cityName='Philadelphia'
            self.name='Phillies'
            self.logo=pygame.image.load('assets\\logos\\PHI_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(232,24,40),(255,255,255)]
        elif abbrev=='PIT':
            self.fullName='Pittsburgh Pirates'
            self.city='Pittsburgh PA'
            self.cityName='Pittsburgh'
            self.name='Pirates'
            self.logo=pygame.image.load('assets\\logos\\PIT_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(253,184,39),(0,0,0)]
        elif abbrev=='STL':
            self.fullName='St. Louis Cardinals'
            self.city='St. Louis, MO'
            self.cityName='St. Louis'
            self.name='Cardinals'
            self.logo=pygame.image.load('assets\\logos\\STL_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(196,30,58),(255,255,255)]
        elif abbrev=='SDP':
            self.fullName='San Diego Padres'
            self.city='San Diego, CA'
            self.cityName='San Diego'
            self.name='Padres'
            self.logo=pygame.image.load('assets\\logos\\SDP_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(0,45,98),(255,255,255)]
        elif abbrev=='SFG':
            self.fullName='San Francisco Giants'
            self.city='San Francisco, CA'
            self.cityName='San Francisco'
            self.name='Giants'
            self.logo=pygame.image.load('assets\\logos\\SFG_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(253,90,30),(0,0,0)]
        elif abbrev=='SEA':
            self.fullName='Seattle Mariners'
            self.city='Seattle, WA'
            self.cityName='Seattle'
            self.name='Mariners'
            self.logo=pygame.image.load('assets\\logos\\SEA_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(12,44,86),(196,206,212)]
        elif abbrev=='TB':
            self.fullName='Tampa Bay Rays'
            self.city='Tampa, FL'
            self.cityName='Tampa Bay'
            self.name='Rays'
            self.logo=pygame.image.load('assets\\logos\\TB_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(9,44,92),(143,188,230)]
        elif abbrev=='TEX':
            self.fullName='Texas Rangers'
            self.city='Dallas, TX'
            self.cityName='Texas'
            self.name='Rangers'
            self.logo=pygame.image.load('assets\\logos\\TEX_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(192,17,31),(0,50,120)]
        elif abbrev=='TOR':
            self.fullName='Toronto Blue Jays'
            self.city='Toronto, ON'
            self.cityName='Toronto'
            self.name='Blue Jays'
            self.logo=pygame.image.load('assets\\logos\\TOR_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(19,74,142),(255,255,255)]
        elif abbrev=='WSH':
            self.fullName='Washington Nationals'
            self.city='Washington, DC'
            self.cityName='Washington'
            self.name='Nationals'
            self.logo=pygame.image.load('assets\\logos\\WSH_logo.png')
            self.logoRatio=self.logo.get_width()/self.logo.get_height()
            self.colors=[(171,0,3),(255,255,255)]
        else:
            raise Exception("Unkown Team")
    def __repr__(self):
        return self.abbrev
    def __eq__(self,other):
        if isinstance(other, str) and self.abbrev==other:
            return True
        elif not isinstance(other, Team):
            return False
        elif self.abbrev==other.abbrev:
            return True
        else:
            return False
    def createRoster(self,names,players):
        result=dict()
        for name in names:
            result[name]=players[name]
        return result

    def getFielders(self,roster):
        fielders=[]
        for player in roster.keys():
            if roster[player].generalPos=='F':
                fielders.append(roster[player])
        return fielders

    def getPitchers(self,roster):
        pitchers=[]
        for player in roster.keys():
            if roster[player].generalPos=='P':
                pitchers.append(roster[player])
        return pitchers

    def getLineup(self,abbrev,roster):
        teamLineup=readFile('assets\\teamData\\lineups\\%s.txt'%abbrev)
        normLineup,names=[],teamLineup.splitlines()
        for i,line in enumerate(names[1:10]):
            info=line.split('\t') 
            #print(info)
            if i!=8:
                normLineup.append((roster[info[0]],info[1]))
            else:
                normLineup.append((info[0],info[1]))
        dhLineup=[]
        for line in names[12:]:
            info=line.split('\t')
            dhLineup.append((roster[info[0]],info[1]))
        return normLineup,dhLineup


    def getRotation(self,abbrev,roster):
        teamRotation=readFile('assets\\teamData\\startingRotations\\%s.txt'%abbrev)
        rotation=[]
        for line in teamRotation.splitlines():
            rotation.append(roster[line])
        return rotation

    def getBench(self,fielders,lineup):
        bench=[]
        for player in fielders:
            bench.append(player)
        for player in lineup:
            if player[0]!='Pitcher':
                #print(bench,player[0])
                bench.remove(player[0])
        return bench

    def getRelievers(self,pitchers,rotation):
        relievers=[]
        for player in pitchers:
            relievers.append(player)
        for player in rotation:
            relievers.remove(player)
        return relievers

def initPlayerLoad(playerFile):
    players=dict()
    allInfo=readFile(playerFile)
    currentPlayer=None
    for line in allInfo.splitlines():
        if line.startswith('Player: '):
            prevPlayer=currentPlayer
            currentPlayer=line[8:]
            if prevPlayer!=None:
                players[prevPlayer]=attributes
            attributes=[]
        elif line.startswith('Num: '):
            attributes.append(line[5:])
        elif line.startswith('Pos: '):
            attributes.append(line[5:])
        elif line.startswith('Rat: '):
            attributes.append(line[5:])
        elif line.startswith('end'):
            players[currentPlayer]=attributes
    return players

class Player(object):
    def __init__(self,name,info):
        self.name=name
        self.pos=info[name][0]
        self.num=info[name][1]
        if self.pos in ['C','1B','2B','3B','SS','LF','CF','RF','DH']:
            self.generalPos='F'
            if self.pos in ['2B','3B','SS']:
                self.posType='INF'
            elif self.pos in ['LF','CF','RF']:
                self.posType='OF'
            else:
                self.posType='C'
            for i,rat in enumerate(info[name][2].split(',')):
                if i==0:
                    self.ovr=int(rat)
                elif i==1:
                    self.con=int(rat)
                elif i==2:
                    self.pow=int(rat)
                elif i==3:
                    self.dsp=int(rat)
                elif i==4:
                    self.spd=int(rat)
                elif i==5:
                    self.fld=int(rat)
            self.conK=self.con/75
            self.powK=self.pow/75
            self.dspK=self.dsp/75
            self.spdK=self.spd/75
            self.fldK=self.fld/75
            self.ctr=0
            self.mov=0
            self.stm=0
            self.pcn=0
            self.ppw=0
            self.ctrK=self.ctr/75
            self.movK=self.mov/75
            self.stmK=self.stm/75
            self.pcnK=self.pcn/75
            self.ppwK=self.ppw/75
        else:
            self.generalPos='P'
            if self.pos in ['RP']:
                self.posType='RP'
            else:
                self.posType='SP'
            for i,rat in enumerate(info[name][2].split(',')):
                if i==0:
                    self.ovr=int(rat)
                elif i==1:
                    self.ctr=int(rat)
                elif i==2:
                    self.mov=int(rat)
                elif i==3:
                    self.stm=int(rat)
                elif i==4:
                    self.pcn=int(rat)
                elif i==5:
                    self.ppw=int(rat)
            self.ctrK=self.ctr/75
            self.movK=self.mov/75
            self.stmK=self.stm/75
            self.pcnK=self.pcn/75
            self.ppwK=self.ppw/75
            self.con=30
            self.pow=30
            self.dsp=30
            self.spd=60
            self.fld=60
            self.conK=self.con/75
            self.powK=self.pow/75
            self.dspK=self.dsp/75
            self.spdK=self.spd/75
            self.fldK=self.fld/75

    def __repr__(self):
        return self.name