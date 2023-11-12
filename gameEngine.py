import random

class Game(object):
    def __init__(self,teams):
        if teams[1] in ['BAL','BOS','CHW','CLE','DET','HOU','KC','LAA','MIN','NYY','OAK','SEA','TB','TEX','TOR']:
            self.dh=True
        else:
            self.dh=False
        self.rotationLoc=random.randint(0,4)
        self.awayTeam=GameTeam(teams[0],self.dh,self.rotationLoc)
        self.homeTeam=GameTeam(teams[1],self.dh,self.rotationLoc)
        self.gameOver=False
        self.outs=0
        self.inning=1
        self.topInning=True
        self.battingTeam=self.awayTeam
        self.pitchingTeam=self.homeTeam
        self.battingTeamIndex=0
        self.pitchingTeamIndex=1
        self.score=[0,0]
        self.inningScore=[[0,0]]
        self.hits=[0,0]
        self.errors=[0,0]
        self.count=[0,0]
        self.bases=[None,None,None]

    def makePitch(self):
        self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].PC+=1
        if self.count[0]==3:
            inStrikeZone=75*self.pitchingTeam.currPitcher.ctrK
        else:
            inStrikeZone=45
        inZone=None
        if random.randint(1,100)<=inStrikeZone: inZone=True
        else: inZone=False
        if inZone:
            swung=None
            if self.count[1]==2:
                swungChance=90
            else:
                swungChance=65
            if random.randint(1,100)<=swungChance: swung=True
            else: swung=False
            if swung:
                contact=None
                if random.randint(1,100)<=87*self.battingTeam.currBatter.conK*self.pitchingTeam.currPitcher.movK: contact=True
                else: contact=False
                if contact:
                    foul=None
                    if random.randint(1,1000)<=482: foul=True
                    else: foul=False
                    if foul:
                        x=random.choice([-13,-7,-3,0,3,7,13])
                        y=-1*(abs(x)+2)
                        if self.count[1]<2:
                            self.count[1]+=1
                            return 'N,%d,%d,10,FOUL'%(x,y)
                        else:
                            return 'N,%d,%d,10,FOUL'%(x,y)
                    else:
                        homerunL=975*(.2*self.battingTeam.currBatter.conK+.8*self.battingTeam.currBatter.powK)*(.8*self.pitchingTeam.currPitcher.ppwK+.2*self.pitchingTeam.currPitcher.conK)
                        homerunLC=1087*(.2*self.battingTeam.currBatter.conK+.8*self.battingTeam.currBatter.powK)*(.8*self.pitchingTeam.currPitcher.ppwK+.2*self.pitchingTeam.currPitcher.conK)
                        homerunC=1031*(.2*self.battingTeam.currBatter.conK+.8*self.battingTeam.currBatter.powK)*(.8*self.pitchingTeam.currPitcher.powK+.2*self.pitchingTeam.currPitcher.conK)
                        homerunRC=922*(.2*self.battingTeam.currBatter.conK+.8*self.battingTeam.currBatter.powK)*(.8*self.pitchingTeam.currPitcher.ppwK+.2*self.pitchingTeam.currPitcher.conK)
                        homerunR=866*(.2*self.battingTeam.currBatter.conK+.8*self.battingTeam.currBatter.powK)*(.8*self.pitchingTeam.currPitcher.ppwK+.2*self.pitchingTeam.currPitcher.conK)
                        tripleL=135*(.4*self.battingTeam.currBatter.powK+.3*self.battingTeam.currBatter.conK+.3*self.battingTeam.currBatter.spdK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.pcnK)
                        tripleLC=152*(.4*self.battingTeam.currBatter.powK+.3*self.battingTeam.currBatter.conK+.3*self.battingTeam.currBatter.spdK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.pcnK)
                        tripleC=145*(.4*self.battingTeam.currBatter.powK+.3*self.battingTeam.currBatter.conK+.3*self.battingTeam.currBatter.spdK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.pcnK)
                        tripleRC=129*(.4*self.battingTeam.currBatter.powK+.3*self.battingTeam.currBatter.conK+.3*self.battingTeam.currBatter.spdK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.pcnK)
                        tripleR=119*(.4*self.battingTeam.currBatter.powK+.3*self.battingTeam.currBatter.conK+.3*self.battingTeam.currBatter.spdK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.pcnK)
                        doubleL=1487*(.5*self.battingTeam.currBatter.conK+.5*self.battingTeam.currBatter.powK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.conK)
                        doubleLC=1649*(.5*self.battingTeam.currBatter.conK+.5*self.battingTeam.currBatter.powK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.conK)
                        doubleC=1570*(.5*self.battingTeam.currBatter.conK+.5*self.battingTeam.currBatter.powK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.conK)
                        doubleRC=1408*(.5*self.battingTeam.currBatter.conK+.5*self.battingTeam.currBatter.powK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.conK)
                        doubleR=1329*(.5*self.battingTeam.currBatter.conK+.5*self.battingTeam.currBatter.powK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.conK)
                        singleL=2352*(.8*self.battingTeam.currBatter.conK+.2*self.battingTeam.currBatter.powK)*(.2*self.pitchingTeam.currPitcher.ppwK+.8*self.pitchingTeam.currPitcher.conK)
                        singleLC=2619*(.8*self.battingTeam.currBatter.conK+.2*self.battingTeam.currBatter.powK)*(.2*self.pitchingTeam.currPitcher.ppwK+.8*self.pitchingTeam.currPitcher.conK)
                        singleC=2484*(.8*self.battingTeam.currBatter.conK+.2*self.battingTeam.currBatter.powK)*(.2*self.pitchingTeam.currPitcher.ppwK+.8*self.pitchingTeam.currPitcher.conK)
                        singleRC=2216*(.8*self.battingTeam.currBatter.conK+.2*self.battingTeam.currBatter.powK)*(.2*self.pitchingTeam.currPitcher.ppwK+.8*self.pitchingTeam.currPitcher.conK)
                        singleR=2081*(.8*self.battingTeam.currBatter.conK+.2*self.battingTeam.currBatter.powK)*(.2*self.pitchingTeam.currPitcher.ppwK+.8*self.pitchingTeam.currPitcher.conK)
                        #single3=2216*self.battingTeam.currBatter.conK*self.pitchingTeam.currPitcher.pcnK
                        single3S=1946*self.battingTeam.currBatter.conK*self.pitchingTeam.currPitcher.pcnK
                        singleS2=3424*self.battingTeam.currBatter.conK*self.pitchingTeam.currPitcher.pcnK
                        single21=1946*self.battingTeam.currBatter.conK*self.pitchingTeam.currPitcher.pcnK
                        #single1=2216*self.battingTeam.currBatter.conK*self.pitchingTeam.currPitcher.pcnK
                        flyoutL=4881*self.battingTeam.currBatter.powK*self.pitchingTeam.currPitcher.ppwK
                        flyoutLC=5491*self.battingTeam.currBatter.powK*self.pitchingTeam.currPitcher.ppwK
                        flyoutC=5186*self.battingTeam.currBatter.powK*self.pitchingTeam.currPitcher.ppwK
                        flyoutRC=4576*self.battingTeam.currBatter.powK*self.pitchingTeam.currPitcher.ppwK
                        flyoutR=4271*self.battingTeam.currBatter.powK*self.pitchingTeam.currPitcher.ppwK
                        lineoutL=1175*(.5*self.battingTeam.currBatter.conK+.5*self.battingTeam.currBatter.powK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.conK)
                        lineoutSS=1443*(.5*self.battingTeam.currBatter.conK+.5*self.battingTeam.currBatter.powK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.conK)
                        lineoutC=1175*(.5*self.battingTeam.currBatter.conK+.5*self.battingTeam.currBatter.powK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.conK)
                        lineout2=1443*(.5*self.battingTeam.currBatter.conK+.5*self.battingTeam.currBatter.powK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.conK)
                        lineoutR=1175*(.5*self.battingTeam.currBatter.conK+.5*self.battingTeam.currBatter.powK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.conK)
                        infieldFly3=746
                        infieldFlySS=746
                        infieldFlyS2=746
                        infieldFly2=746
                        infieldFly1=746
                        groundout3=3570/self.battingTeam.currBatter.powK/self.pitchingTeam.currPitcher.ppwK
                        groundout3S=4544/self.battingTeam.currBatter.powK/self.pitchingTeam.currPitcher.ppwK
                        groundoutSS=5517/self.battingTeam.currBatter.powK/self.pitchingTeam.currPitcher.ppwK
                        groundoutS2=4544/self.battingTeam.currBatter.powK/self.pitchingTeam.currPitcher.ppwK
                        groundout2=4544/self.battingTeam.currBatter.powK/self.pitchingTeam.currPitcher.ppwK
                        groundout21=4219/self.battingTeam.currBatter.powK/self.pitchingTeam.currPitcher.ppwK
                        groundout1=2921/self.battingTeam.currBatter.powK/self.pitchingTeam.currPitcher.ppwK
                        groundoutCa=1298/self.battingTeam.currBatter.powK/self.pitchingTeam.currPitcher.ppwK
                        groundoutP=1298/self.battingTeam.currBatter.powK/self.pitchingTeam.currPitcher.ppwK
                        total=1
                        overall=homerunL+homerunLC+homerunC+homerunRC+homerunR+tripleL+tripleLC+tripleC+tripleRC+tripleR+doubleL+doubleLC+doubleC+doubleRC+doubleR+singleL+singleLC+singleC+singleRC+singleR+single3S+singleS2+single21+flyoutL+flyoutLC+flyoutC+flyoutRC+flyoutR+lineoutL+lineoutSS+lineoutC+lineout2+lineoutR+groundout3+groundout3S+groundoutSS+groundoutS2+groundout2+groundout21+groundout1+groundoutCa+groundoutP
                        x=random.randint(1,int(overall))
                        #HOMERUN
                        if total<=x<homerunL:
                            return self.homerun('L')
                        else: total+=homerunL
                        if total<=x<total+homerunLC:
                            return self.homerun('LC')
                        else: total+=homerunLC
                        if total<=x<total+homerunC:
                            return self.homerun('C')
                        else: total+=homerunC
                        if total<=x<total+homerunRC:
                            return self.homerun('RC')
                        else: total+=homerunRC
                        if total<=x<total+homerunR:
                            return self.homerun('R')
                        else: total+=homerunR
                        #TRIPLE
                        if total<=x<total+tripleL:
                            return self.triple('L')
                        else: total+=tripleL
                        if total<=x<total+tripleLC:
                            return self.triple('LC')
                        else: total+=tripleLC
                        if total<=x<total+tripleC:
                            return self.triple('C')
                        else: total+=tripleC
                        if total<=x<total+tripleRC:
                            return self.triple('RC')
                        else: total+=tripleRC
                        if total<=x<total+tripleR:
                            return self.triple('R')
                        else: total+=tripleR
                        #DOUBLE
                        if total<=x<total+doubleL:
                            return self.double('L')
                        else: total+=doubleL
                        if total<=x<total+doubleLC:
                            return self.double('LC')
                        else: total+=doubleLC
                        if total<=x<total+doubleC:
                            return self.double('C')
                        else: total+=doubleC
                        if total<=x<total+doubleRC:
                            return self.double('RC')
                        else: total+=doubleRC
                        if total<=x<total+doubleR:
                            return self.double('R')
                        else: total+=doubleR
                        #SINGLE
                        if total<=x<total+singleL:
                            return self.single('L')
                        else: total+=singleL
                        if total<=x<total+singleLC:
                            return self.single('LC')
                        else: total+=singleLC
                        if total<=x<total+singleC:
                            return self.single('C')
                        else: total+=singleC
                        if total<=x<total+singleRC:
                            return self.single('RC')
                        else: total+=singleRC
                        if total<=x<total+singleR:
                            return self.single('R')
                        else: total+=singleR
                        # if total<=x<total+single3:
                        #     return self.single('3')
                        # else: total+=single3
                        if total<=x<total+single3S:
                            return self.single('3S')
                        else: total+=single3S
                        if total<=x<total+singleS2:
                            return self.single('S2')
                        else: total+=singleS2
                        if total<=x<total+single21:
                            return self.single('21')
                        else: total+=single21
                        # if total<=x<total+single1:
                        #     return self.single('1')
                        # else: total+=single1
                        #FLYOUT
                        if total<=x<total+flyoutL:
                            return self.flyout('L')
                        else: total+=flyoutL
                        if total<=x<total+flyoutLC:
                            return self.flyout('LC')
                        else: total+=flyoutLC
                        if total<=x<total+flyoutC:
                            return self.flyout('C')
                        else: total+=flyoutC
                        if total<=x<total+flyoutRC:
                            return self.flyout('RC')
                        else: total+=flyoutRC
                        if total<=x<total+flyoutR:
                            return self.flyout('R')
                        else: total+=flyoutR
                        #LINEOUT
                        if total<=x<total+lineoutL:
                            return self.lineout('L')
                        else: total+=lineoutL
                        if total<=x<total+lineoutSS:
                            return self.lineout('SS')
                        else: total+=lineoutSS
                        if total<=x<total+lineoutC:
                            return self.lineout('C')
                        else: total+=lineoutC
                        if total<=x<total+lineout2:
                            return self.lineout('2')
                        else: total+=lineout2
                        if total<=x<total+lineoutR:
                            return self.lineout('R')
                        else: total+=lineoutR
                        #INFIELDFLY
                        if total<=x<total+infieldFly3:
                            return self.infieldFly('3')
                        else: total+=infieldFly3
                        if total<=x<total+infieldFlySS:
                            return self.infieldFly('SS')
                        else: total+=infieldFlySS
                        if total<=x<total+infieldFlyS2:
                            return self.infieldFly('S2')
                        else: total+=infieldFlyS2
                        if total<=x<total+infieldFly2:
                            return self.infieldFly('2')
                        else: total+=infieldFly2
                        if total<=x<total+infieldFly1:
                            return self.infieldFly('1')
                        else: total+=infieldFly1
                        #GROUNDOUT
                        if total<=x<total+groundout3:
                            return self.groundout('3')
                        else: total+=groundout3
                        if total<=x<total+groundout3S:
                            return self.groundout('3S')
                        else: total+=groundout3S
                        if total<=x<total+groundoutSS:
                            return self.groundout('SS')
                        else: total+=groundoutSS
                        if total<=x<total+groundoutS2:
                            return self.groundout('S2')
                        else: total+=groundoutS2
                        if total<=x<total+groundout2:
                            return self.groundout('2')
                        else: total+=groundout2
                        if total<=x<total+groundout21:
                            return self.groundout('21')
                        else: total+=groundout21
                        if total<=x<total+groundout1:
                            return self.groundout('1')
                        else: total+=groundout1
                        if total<=x<total+groundoutCa:
                            return self.groundout('Ca')
                        else: total+=groundoutCa
                        if total<=x<total+groundoutP:
                            return self.groundout('P')
                        else: total+=groundoutP
                else:
                    self.count[1]+=1
                    if self.count[1]>=3:
                        self.strikeout()
                        return 'N,0,0,0,STRIKEOUT SWINGING'
                    else:
                        return 'N,0,0,0,STRIKE SWINGING'
            else:
                self.count[1]+=1
                if self.count[1]>=3:
                    self.strikeout()
                    return 'N,0,0,0,STRIKEOUT LOOKING'
                else:
                    return 'N,0,0,0,STRIKE LOOKING'
        else:
            swung=None
            if random.randint(1,100)<=30/self.battingTeam.currBatter.dspK*self.pitchingTeam.currPitcher.movK: swung=True
            else: swung=False
            if swung:
                contact=None
                if random.randint(1,100)<=75*self.battingTeam.currBatter.conK*self.pitchingTeam.currPitcher.movK: contact=True
                else: contact=False
                if contact:
                    foul=None
                    if random.randint(1,1000)<=482: foul=True
                    else: foul=False
                    if foul:
                        x=random.choice([-13,-7,-3,0,3,7,13])
                        y=-1*(abs(x)+2)
                        if self.count[1]<2:
                            self.count[1]+=1
                            return 'N,%d,%d,10,FOUL'%(x,y)
                        else:
                            return 'N,%d,%d,10,FOUL'%(x,y)
                    else:
                        homerunL=975*(.2*self.battingTeam.currBatter.conK+.8*self.battingTeam.currBatter.powK)*(.8*self.pitchingTeam.currPitcher.ppwK+.2*self.pitchingTeam.currPitcher.conK)*.5
                        homerunLC=1087*(.2*self.battingTeam.currBatter.conK+.8*self.battingTeam.currBatter.powK)*(.8*self.pitchingTeam.currPitcher.ppwK+.2*self.pitchingTeam.currPitcher.conK)*.5
                        homerunC=1031*(.2*self.battingTeam.currBatter.conK+.8*self.battingTeam.currBatter.powK)*(.8*self.pitchingTeam.currPitcher.ppwK+.2*self.pitchingTeam.currPitcher.conK)*.5
                        homerunRC=922*(.2*self.battingTeam.currBatter.conK+.8*self.battingTeam.currBatter.powK)*(.8*self.pitchingTeam.currPitcher.ppwK+.2*self.pitchingTeam.currPitcher.conK)*.5
                        homerunR=866*(.2*self.battingTeam.currBatter.conK+.8*self.battingTeam.currBatter.powK)*(.8*self.pitchingTeam.currPitcher.ppwK+.2*self.pitchingTeam.currPitcher.conK)*.5
                        tripleL=135*(.4*self.battingTeam.currBatter.powK+.3*self.battingTeam.currBatter.conK+.3*self.battingTeam.currBatter.spdK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.pcnK)*.5
                        tripleLC=152*(.4*self.battingTeam.currBatter.powK+.3*self.battingTeam.currBatter.conK+.3*self.battingTeam.currBatter.spdK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.pcnK)*.5
                        tripleC=145*(.4*self.battingTeam.currBatter.powK+.3*self.battingTeam.currBatter.conK+.3*self.battingTeam.currBatter.spdK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.pcnK)*.5
                        tripleRC=129*(.4*self.battingTeam.currBatter.powK+.3*self.battingTeam.currBatter.conK+.3*self.battingTeam.currBatter.spdK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.pcnK)*.5
                        tripleR=119*(.4*self.battingTeam.currBatter.powK+.3*self.battingTeam.currBatter.conK+.3*self.battingTeam.currBatter.spdK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.pcnK)*.5
                        doubleL=1487*(.5*self.battingTeam.currBatter.conK+.5*self.battingTeam.currBatter.powK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.conK)*.5
                        doubleLC=1649*(.5*self.battingTeam.currBatter.conK+.5*self.battingTeam.currBatter.powK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.conK)*.5
                        doubleC=1570*(.5*self.battingTeam.currBatter.conK+.5*self.battingTeam.currBatter.powK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.conK)*.5
                        doubleRC=1408*(.5*self.battingTeam.currBatter.conK+.5*self.battingTeam.currBatter.powK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.conK)*.5
                        doubleR=1329*(.5*self.battingTeam.currBatter.conK+.5*self.battingTeam.currBatter.powK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.conK)*.5
                        singleL=2352*(.8*self.battingTeam.currBatter.conK+.2*self.battingTeam.currBatter.powK)*(.2*self.pitchingTeam.currPitcher.ppwK+.8*self.pitchingTeam.currPitcher.conK)*.5
                        singleLC=2619*(.8*self.battingTeam.currBatter.conK+.2*self.battingTeam.currBatter.powK)*(.2*self.pitchingTeam.currPitcher.ppwK+.8*self.pitchingTeam.currPitcher.conK)*.5
                        singleC=2484*(.8*self.battingTeam.currBatter.conK+.2*self.battingTeam.currBatter.powK)*(.2*self.pitchingTeam.currPitcher.ppwK+.8*self.pitchingTeam.currPitcher.conK)*.5
                        singleRC=2216*(.8*self.battingTeam.currBatter.conK+.2*self.battingTeam.currBatter.powK)*(.2*self.pitchingTeam.currPitcher.ppwK+.8*self.pitchingTeam.currPitcher.conK)*.5
                        singleR=2081*(.8*self.battingTeam.currBatter.conK+.2*self.battingTeam.currBatter.powK)*(.2*self.pitchingTeam.currPitcher.ppwK+.8*self.pitchingTeam.currPitcher.conK)*.5
                        #single3=2216*self.battingTeam.currBatter.conK*self.pitchingTeam.currPitcher.pcnK*.5
                        single3S=1946*self.battingTeam.currBatter.conK*self.pitchingTeam.currPitcher.pcnK*.5
                        singleS2=3424*self.battingTeam.currBatter.conK*self.pitchingTeam.currPitcher.pcnK*.5
                        single21=1946*self.battingTeam.currBatter.conK*self.pitchingTeam.currPitcher.pcnK*.5
                        #single1=2216*self.battingTeam.currBatter.conK*self.pitchingTeam.currPitcher.pcnK*.5
                        flyoutL=4881*self.battingTeam.currBatter.powK*self.pitchingTeam.currPitcher.ppwK*2
                        flyoutLC=5491*self.battingTeam.currBatter.powK*self.pitchingTeam.currPitcher.ppwK*2
                        flyoutC=5186*self.battingTeam.currBatter.powK*self.pitchingTeam.currPitcher.ppwK*2
                        flyoutRC=4576*self.battingTeam.currBatter.powK*self.pitchingTeam.currPitcher.ppwK*2
                        flyoutR=4271*self.battingTeam.currBatter.powK*self.pitchingTeam.currPitcher.ppwK*2
                        lineoutL=1175*(.5*self.battingTeam.currBatter.conK+.5*self.battingTeam.currBatter.powK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.conK)*2
                        lineoutSS=1443*(.5*self.battingTeam.currBatter.conK+.5*self.battingTeam.currBatter.powK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.conK)*2
                        lineoutC=1175*(.5*self.battingTeam.currBatter.conK+.5*self.battingTeam.currBatter.powK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.conK)*2
                        lineout2=1443*(.5*self.battingTeam.currBatter.conK+.5*self.battingTeam.currBatter.powK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.conK)*2
                        lineoutR=1175*(.5*self.battingTeam.currBatter.conK+.5*self.battingTeam.currBatter.powK)*(.5*self.pitchingTeam.currPitcher.ppwK+.5*self.pitchingTeam.currPitcher.conK)*2
                        infieldFly3=746*2
                        infieldFlySS=746*2
                        infieldFlyS2=746*2
                        infieldFly2=746*2
                        infieldFly1=746*2
                        groundout3=3570/self.battingTeam.currBatter.powK/self.pitchingTeam.currPitcher.ppwK*2
                        groundout3S=4544/self.battingTeam.currBatter.powK/self.pitchingTeam.currPitcher.ppwK*2
                        groundoutSS=5517/self.battingTeam.currBatter.powK/self.pitchingTeam.currPitcher.ppwK*2
                        groundoutS2=4544/self.battingTeam.currBatter.powK/self.pitchingTeam.currPitcher.ppwK*2
                        groundout2=4544/self.battingTeam.currBatter.powK/self.pitchingTeam.currPitcher.ppwK*2
                        groundout21=4219/self.battingTeam.currBatter.powK/self.pitchingTeam.currPitcher.ppwK*2
                        groundout1=2921/self.battingTeam.currBatter.powK/self.pitchingTeam.currPitcher.ppwK*2
                        groundoutCa=1298/self.battingTeam.currBatter.powK/self.pitchingTeam.currPitcher.ppwK*2
                        groundoutP=1298/self.battingTeam.currBatter.powK/self.pitchingTeam.currPitcher.ppwK*2
                        total=1
                        overall=homerunL+homerunLC+homerunC+homerunRC+homerunR+tripleL+tripleLC+tripleC+tripleRC+tripleR+doubleL+doubleLC+doubleC+doubleRC+doubleR+singleL+singleLC+singleC+singleRC+singleR+single3S+singleS2+single21+flyoutL+flyoutLC+flyoutC+flyoutRC+flyoutR+lineoutL+lineoutSS+lineoutC+lineout2+lineoutR+groundout3+groundout3S+groundoutSS+groundoutS2+groundout2+groundout21+groundout1+groundoutCa+groundoutP
                        x=random.randint(1,int(overall))
                        #HOMERUN
                        if total<=x<homerunL:
                            return self.homerun('L')
                        else: total+=homerunL
                        if total<=x<total+homerunLC:
                            return self.homerun('LC')
                        else: total+=homerunLC
                        if total<=x<total+homerunC:
                            return self.homerun('C')
                        else: total+=homerunC
                        if total<=x<total+homerunRC:
                            return self.homerun('RC')
                        else: total+=homerunRC
                        if total<=x<total+homerunR:
                            return self.homerun('R')
                        else: total+=homerunR
                        #TRIPLE
                        if total<=x<total+tripleL:
                            return self.triple('L')
                        else: total+=tripleL
                        if total<=x<total+tripleLC:
                            return self.triple('LC')
                        else: total+=tripleLC
                        if total<=x<total+tripleC:
                            return self.triple('C')
                        else: total+=tripleC
                        if total<=x<total+tripleRC:
                            return self.triple('RC')
                        else: total+=tripleRC
                        if total<=x<total+tripleR:
                            return self.triple('R')
                        else: total+=tripleR
                        #DOUBLE
                        if total<=x<total+doubleL:
                            return self.double('L')
                        else: total+=doubleL
                        if total<=x<total+doubleLC:
                            return self.double('LC')
                        else: total+=doubleLC
                        if total<=x<total+doubleC:
                            return self.double('C')
                        else: total+=doubleC
                        if total<=x<total+doubleRC:
                            return self.double('RC')
                        else: total+=doubleRC
                        if total<=x<total+doubleR:
                            return self.double('R')
                        else: total+=doubleR
                        #SINGLE
                        if total<=x<total+singleL:
                            return self.single('L')
                        else: total+=singleL
                        if total<=x<total+singleLC:
                            return self.single('LC')
                        else: total+=singleLC
                        if total<=x<total+singleC:
                            return self.single('C')
                        else: total+=singleC
                        if total<=x<total+singleRC:
                            return self.single('RC')
                        else: total+=singleRC
                        if total<=x<total+singleR:
                            return self.single('R')
                        else: total+=singleR
                        # if total<=x<total+single3:
                        #     return self.single('3')
                        # else: total+=single3
                        if total<=x<total+single3S:
                            return self.single('3S')
                        else: total+=single3S
                        if total<=x<total+singleS2:
                            return self.single('S2')
                        else: total+=singleS2
                        if total<=x<total+single21:
                            return self.single('21')
                        else: total+=single21
                        # if total<=x<total+single1:
                        #     return self.single('1')
                        # else: total+=single1
                        #FLYOUT
                        if total<=x<total+flyoutL:
                            return self.flyout('L')
                        else: total+=flyoutL
                        if total<=x<total+flyoutLC:
                            return self.flyout('LC')
                        else: total+=flyoutLC
                        if total<=x<total+flyoutC:
                            return self.flyout('C')
                        else: total+=flyoutC
                        if total<=x<total+flyoutRC:
                            return self.flyout('RC')
                        else: total+=flyoutRC
                        if total<=x<total+flyoutR:
                            return self.flyout('R')
                        else: total+=flyoutR
                        #LINEOUT
                        if total<=x<total+lineoutL:
                            return self.lineout('L')
                        else: total+=lineoutL
                        if total<=x<total+lineoutSS:
                            return self.lineout('SS')
                        else: total+=lineoutSS
                        if total<=x<total+lineoutC:
                            return self.lineout('C')
                        else: total+=lineoutC
                        if total<=x<total+lineout2:
                            return self.lineout('2')
                        else: total+=lineout2
                        if total<=x<total+lineoutR:
                            return self.lineout('R')
                        else: total+=lineoutR
                        #INFIELDFLY
                        if total<=x<total+infieldFly3:
                            return self.infieldFly('3')
                        else: total+=infieldFly3
                        if total<=x<total+infieldFlySS:
                            return self.infieldFly('SS')
                        else: total+=infieldFlySS
                        if total<=x<total+infieldFlyS2:
                            return self.infieldFly('S2')
                        else: total+=infieldFlyS2
                        if total<=x<total+infieldFly2:
                            return self.infieldFly('2')
                        else: total+=infieldFly2
                        if total<=x<total+infieldFly1:
                            return self.infieldFly('1')
                        else: total+=infieldFly1
                        #GROUNDOUT
                        if total<=x<total+groundout3:
                            return self.groundout('3')
                        else: total+=groundout3
                        if total<=x<total+groundout3S:
                            return self.groundout('3S')
                        else: total+=groundout3S
                        if total<=x<total+groundoutSS:
                            return self.groundout('SS')
                        else: total+=groundoutSS
                        if total<=x<total+groundoutS2:
                            return self.groundout('S2')
                        else: total+=groundoutS2
                        if total<=x<total+groundout2:
                            return self.groundout('2')
                        else: total+=groundout2
                        if total<=x<total+groundout21:
                            return self.groundout('21')
                        else: total+=groundout21
                        if total<=x<total+groundout1:
                            return self.groundout('1')
                        else: total+=groundout1
                        if total<=x<total+groundoutCa:
                            return self.groundout('Ca')
                        else: total+=groundoutCa
                        if total<=x<total+groundoutP:
                            return self.groundout('P')
                        else: total+=groundoutP
                else:
                    self.count[1]+=1
                    if self.count[1]>=3:
                        self.strikeout()
                        return 'N,0,0,0,STRIKEOUT SWINGING'
                    else:
                        return 'N,0,0,0,STRIKE SWINGING'
            else:
                self.count[0]+=1
                if self.count[0]>=4:
                    self.walk()
                    return 'N,0,0,0,WALK'
                else:
                    return 'N,0,0,0,BALL'

    def checkGameStatus(self):
        if self.outs>=3:
            if self.inning+1>9 and not self.topInning and self.score[0]!=self.score[1]:
                self.gameOver=True
            self.changeInning()
        if not self.topInning and self.inning>=9 and self.score[1]>self.score[0]:
            if self.inningScore[-1][1]==0:
                self.inningScore[-1][1]='x'
            self.gameOver=True

    def changeInning(self):
        self.battingTeam.checkPlayers()
        self.pitchingTeam.checkPlayers()
        self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].getIP()
        self.outs=0
        self.topInning=not self.topInning
        if self.topInning:
            self.inning+=1
        self.bases=[None,None,None]
        self.battingTeam,self.pitchingTeam=self.pitchingTeam,self.battingTeam
        self.battingTeamIndex,self.pitchingTeamIndex=self.pitchingTeamIndex,self.battingTeamIndex
        if not self.gameOver and self.topInning:
            self.inningScore.append([0,0])

    def changeBatter(self):
        self.count=[0,0]
        self.battingTeam.index+=1
        self.battingTeam.currBatter=self.battingTeam.lineup[self.battingTeam.index%len(self.battingTeam.lineup)]

    def homerun(self, location):
        for runner in self.bases:
            if runner!=None:
                self.score[self.battingTeamIndex]+=1
                self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].RBI+=1
                self.battingTeam.inGamePlayers[runner.name].R+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].ER+=1
        self.score[self.battingTeamIndex]+=1
        self.inningScore[self.inning-1][self.battingTeamIndex]+=1
        self.hits[self.battingTeamIndex]+=1
        self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].H+=1
        self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].AB+=1
        self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].HR+=1
        self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].RBI+=1
        self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].R+=1
        self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].HA+=1
        self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
        self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].ER+=1
        self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].HRA+=1
        self.bases=[None,None,None]
        self.changeBatter()
        self.checkGameStatus()
        if location=='L':
            return 'Y,-5,5,16,HOMERUN'
        elif location=='LC':
            return 'Y,-3,5,17,HOMERUN'
        elif location=='C':
            return 'Y,0,6,15,HOMERUN'
        elif location=='RC':
            return 'Y,3,5,17,HOMERUN'
        elif location=='R':
            return 'Y,5,5,16,HOMERUN'
        else:
            return 'Y,2,5,17,HOMERUN'

    def triple(self, location):
        for runner in self.bases:
            if runner!=None:
                self.score[self.battingTeamIndex]+=1
                self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].RBI+=1
                self.battingTeam.inGamePlayers[runner.name].R+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].ER+=1
        self.bases=[None,None,self.battingTeam.currBatter]
        self.hits[self.battingTeamIndex]+=1
        self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].H+=1
        self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].AB+=1
        self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].t+=1
        self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].HA+=1
        self.changeBatter()
        self.checkGameStatus()
        if location=='L':
            return 'Y,-8,7,9,TRIPLE'
        elif location=='LC':
            return 'Y,-3,8,9,TRIPLE'
        elif location=='C':
            return 'Y,-1.5,8,9.5,TRIPLE'
        elif location=='RC':
            return 'Y,3,8,9,TRIPLE'
        elif location=='R':
            return 'Y,9,8,8,TRIPLE'
        else:
            return 'Y,2,8,8,TRIPLE'

    def double(self, location):
        if self.bases[2]!=None:
            self.score[self.battingTeamIndex]+=1
            self.inningScore[self.inning-1][self.battingTeamIndex]+=1
            self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].RBI+=1
            self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
            self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
            self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].ER+=1
            self.bases[2]=None
        if self.bases[1]!=None:
            self.score[self.battingTeamIndex]+=1
            self.inningScore[self.inning-1][self.battingTeamIndex]+=1
            self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].RBI+=1
            self.battingTeam.inGamePlayers[self.bases[1].name].R+=1
            self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
            self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].ER+=1
            self.bases[1]=None
        if self.bases[0]!=None:
            x=random.randint(1,100)
            if x<40:
                self.bases[2]=self.bases[0]
                self.bases[0]=None
            else:
                self.score[self.battingTeamIndex]+=1
                self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].RBI+=1
                self.battingTeam.inGamePlayers[self.bases[0].name].R+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].ER+=1
                self.bases[0]=None
        self.bases[1]=self.battingTeam.currBatter
        self.hits[self.battingTeamIndex]+=1
        self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].H+=1
        self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].AB+=1
        self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].d+=1
        self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].HA+=1
        self.changeBatter()
        self.checkGameStatus()
        if location=='L':
            return 'Y,-7,6.5,9,DOUBLE'
        elif location=='LC':
            return 'Y,-3.5,9,8,DOUBLE'
        elif location=='C':
            return 'Y,2,8,9,DOUBLE'
        elif location=='RC':
            return 'Y,3,8,9,DOUBLE'
        elif location=='R':
            return 'Y,7,7,9,DOUBLE'
        else:
            return 'Y,2,8,9,DOUBLE'

    def single(self, location):
        if self.bases[2]!=None:
            self.score[self.battingTeamIndex]+=1
            self.inningScore[self.inning-1][self.battingTeamIndex]+=1
            self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].RBI+=1
            self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
            self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
            self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].ER+=1
            self.bases[2]=None
        if self.bases[1]!=None:
            x=random.randint(1,100)
            if x<50:
                self.bases[2]=self.bases[1]
                self.bases[1]=None
            else:
                self.score[self.battingTeamIndex]+=1
                self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].RBI+=1
                self.battingTeam.inGamePlayers[self.bases[1].name].R+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].ER+=1
                self.bases[1]=None
        if self.bases[0]!=None:
            x=random.randint(1,100)
            if x<50 and self.bases[2]==None:
                self.bases[2]=self.bases[0]
                self.bases[0]=None
            else:
                self.bases[1]=self.bases[0]
                self.bases[0]=None
        self.bases[0]=self.battingTeam.currBatter
        self.hits[self.battingTeamIndex]+=1
        self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].H+=1
        self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].AB+=1
        self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].HA+=1
        self.changeBatter()
        self.checkGameStatus()
        if location=='L':
            return 'Y,-5,8,8,SINGLE'
        elif location=='LC':
            return 'Y,-2,8,8,SINGLE'
        elif location=='C':
            return 'Y,0,8,8,SINGLE'
        elif location=='RC':
            return 'Y,2,8,8,SINGLE'
        elif location=='R':
            return 'Y,5,8,8,SINGLE'
        # elif location=='3':
        #     return 'Y,-5.5,8,5,SINGLE'
        elif location=='3S':
            return 'Y,-2.5,5,2,SINGLE'
        elif location=='S2':
            return 'Y,0,8,5,SINGLE'
        elif location=='21':
            return 'Y,3.5,8,7,SINGLE'
        # elif location=='1':
        #     return 'Y,5.5,8,7,SINGLE'
        else:
            return 'Y,0,8,7,SINGLE'

    def flyout(self, location):
        result='FLYOUT'
        x=random.randint(1,100)
        if x<99:
            self.outs+=1
            if self.outs<3 and self.bases[2]!=None:
                x=random.randint(1,100)
                if x<70:
                    self.score[self.battingTeamIndex]+=1
                    self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                    self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].RBI+=1
                    self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
                    self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
                    self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].ER+=1
                    self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].AB-=1
                    self.bases[2]=None
                    result='SAC FLY'
                    if self.bases[1]!=None:
                        x=random.randint(1,100)
                        if x<90:
                            self.bases[2]=self.bases[1]
                            self.bases[1]=None
                else:
                    result='FLYOUT'
            else:
                result='FLYOUT'
        else:
            result='ERROR'
            if self.bases[2]!=None:
                self.score[self.battingTeamIndex]+=1
                self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
            self.bases[2]=self.bases[1]
            self.bases[1]=self.bases[0]
            self.bases[0]=self.battingTeam.currBatter
            self.errors[self.pitchingTeamIndex]+=1
            self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS-=1
        self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS+=1
        self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].AB+=1
        self.changeBatter()
        self.checkGameStatus()
        if location=='L':
            return 'Y,-4,4,15,%s'%result
        elif location=='LC':
            return 'Y,-1.7,5,15,%s'%result
        elif location=='C':
            return 'Y,0,5,15,%s'%result
        elif location=='RC':
            return 'Y,1.7,5,15,%s'%result
        elif location=='R':
            return 'Y,4.4,4,15,%s'%result
        else:
            return 'Y,3,4,15,%s'%result

    def lineout(self, location):
        x=random.randint(1,100)
        result='LINEOUT'
        if x<3*self.battingTeam.currBatter.conK:
            result='ERROR'
            if self.bases[2]!=None:
                self.score[self.battingTeamIndex]+=1
                self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
            self.bases[2]=self.bases[1]
            self.bases[1]=self.bases[0]
            self.bases[0]=self.battingTeam.currBatter
            self.errors[self.pitchingTeamIndex]+=1
            self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS-=1
        else:
            self.outs+=1
            result='LINEOUT'
        self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].AB+=1
        self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS+=1
        self.changeBatter()
        self.checkGameStatus()
        if location=='L':
            return 'Y,-5,5,5,%s'%result
        elif location=='SS':
            return 'Y,-2.5,5,3,%s'%result
        elif location=='C':
            return 'Y,0,8,9,%s'%result
        elif location=='2':
            return 'Y,2,5,3,%s'%result
        elif location=='R':
            return 'Y,5,5,5,%s'%result
        else:
            return 'Y,2,5,5,%s'%result

    def infieldFly(self, location):
        self.outs+=1
        self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].AB+=1
        self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS+=1
        self.changeBatter()
        self.checkGameStatus()
        if location=='3':
            return 'Y,-2,2,13,INFIELD FLYOUT'
        elif location=='SS':
            return 'Y,-1,2,13,INFIELD FLYOUT'
        elif location=='S2':
            return 'Y,0,4,13,INFIELD FLYOUT'
        elif location=='2':
            return 'Y,1,2,13,INFIELD FLYOUT'
        elif location=='1':
            return 'Y,2,2,13,INFIELD FLYOUT'
        else:
            return 'Y,1,3,13,INFIELD FLYOUT'

    def groundout(self, location):
        result='GROUNDOUT'
        if self.outs==2:
            x=random.randint(1,100)
            if x>96:
                result='ERROR'
                self.errors[self.pitchingTeamIndex]+=1
                if self.bases[2]!=None:
                    self.score[self.battingTeamIndex]+=1
                    self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                    self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
                    self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
                self.bases[2]=self.bases[1]
                self.bases[1]=self.bases[0]
                self.bases[0]=self.battingTeam.currBatter
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS-=1
            else:
                self.outs+=1
                result='GROUNDOUT'
        elif self.bases[2]!= None and self.bases[1]!=None and self.bases[0]!=None:
            x=random.randint(1,100)
            if x<35:
                self.score[self.battingTeamIndex]+=1
                self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].ER+=1
                self.bases[2]=self.bases[1]
                self.bases[1]=None
                self.bases[0]=None
                self.outs+=2
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS+=1
                result='DOUBLE PLAY'
            elif x<50:
                self.bases[2]=self.bases[1]
                self.bases[1]=self.bases[0]
                self.bases[0]=None
                self.outs+=2
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS+=1
                result='DOUBLE PLAY'
            elif x<75:
                self.bases[2]=self.bases[1]
                self.bases[1]=self.bases[0]
                self.bases[0]=self.battingTeam.currBatter
                self.outs+=1
                result='FIELDER\'S CHOICE'
            else:
                self.score[self.battingTeamIndex]+=1
                self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].RBI+=1
                self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].ER+=1
                self.bases[2]=self.bases[1]
                self.bases[1]=self.bases[0]
                self.bases[0]=None
                self.outs+=1
                result='GROUNDOUT'
        elif self.bases[2]!=None and self.bases[1]!=None and self.bases[0]==None:
            x=random.randint(1,100)
            if x<40:
                self.outs+=1
                result='GROUNDOUT'
            elif x<65:
                self.score[self.battingTeamIndex]+=1
                self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].RBI+=1
                self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].ER+=1
                self.bases[2]=self.bases[1]
                self.bases[1]=None
                self.bases[0]=None
                self.outs+=1
                result='GROUNDOUT'
            elif x<80:
                self.bases[2]=self.bases[1]
                self.bases[1]=None
                self.bases[0]=self.battingTeam.currBatter
                self.outs+=1
                result='FIELDER\'S CHOICE'
            elif x<96:
                self.bases[2]=None
                self.bases[0]=self.battingTeam.currBatter
                self.outs+=1
                result='FIELDER\'S CHOICE'
            else:
                self.score[self.battingTeamIndex]+=1
                self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
                self.bases[2]=self.bases[1]
                self.bases[1]=self.bases[0]
                self.bases[0]=self.battingTeam.currBatter
                self.errors[self.pitchingTeamIndex]+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS-=1
                result='ERROR'
        elif self.bases[2]!=None and self.bases[1]==None and self.bases[0]!=None:
            x=random.randint(1,100)
            if x<35:
                self.outs+=2
                self.score[self.battingTeamIndex]+=1
                self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].ER+=1
                self.bases=[None,None,None]
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS+=1
                result='DOUBLE PLAY'
            elif x<52:
                self.score[self.battingTeamIndex]+=1
                self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].RBI+=1
                self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].ER+=1
                self.bases[2]=None
                self.bases[1]=None
                self.bases[0]=self.battingTeam.currBatter
                self.outs+=1
                result='FIELDER\'S CHOICE'
            elif x<70:
                self.score[self.battingTeamIndex]+=1
                self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].RBI+=1
                self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].ER+=1
                self.bases[2]=self.bases[1]
                self.bases[1]=self.bases[0]
                self.bases[0]=None
                self.outs+=1
                result='GROUNDOUT'
            elif x<96:
                self.bases[1]=self.bases[0]
                self.bases[0]=None
                self.outs+=1
                result='GROUNDOUT'
            else:
                self.score[self.battingTeamIndex]+=1
                self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
                self.bases[2]=self.bases[1]
                self.bases[1]=self.bases[0]
                self.bases[0]=self.battingTeam.currBatter
                self.errors[self.pitchingTeamIndex]+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS-=1
                result='ERROR' 
        elif self.bases[2]!=None and self.bases[1]==None and self.bases[0]==None:
            x=random.randint(1,100)
            if x<40:
                self.outs+=1
                self.score[self.battingTeamIndex]+=1
                self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].RBI+=1
                self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].ER+=1
                self.bases[2]=None
                result='GROUNDOUT'
            elif x<80:
                self.outs+=1
                result='GROUNDOUT'
            elif x<96:
                self.bases[2]=None
                self.bases[0]=self.battingTeam.currBatter
                self.outs+=1
                result='FIELDER\'S CHOICE'
            else:
                if self.bases[2]!=None:
                    self.score[self.battingTeamIndex]+=1
                    self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                    self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
                    self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
                self.bases[2]=self.bases[1]
                self.bases[1]=self.bases[0]
                self.bases[0]=self.battingTeam.currBatter
                self.errors[self.pitchingTeamIndex]+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS-=1
                result='ERROR'
        elif self.bases[2]==None and self.bases[1]!=None and self.bases[0]!=None:
            x=random.randint(1,100)
            if x<5 and self.outs==0:
                self.outs+=3
                self.bases=[None,None,None]
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS+=2
                result='TRIPLE PLAY'
            elif x<15:
                self.outs+=2
                self.bases[2]=None
                self.bases[1]=self.bases[0]
                self.bases[0]=None
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS+=1
                result='DOUBLE PLAY'
            elif x<60:
                self.bases[2]=self.bases[1]
                self.bases[1]=None
                self.bases[0]=None
                self.outs+=2
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS+=1
                result='DOUBLE PLAY'
            elif x<75:
                self.outs+=1
                self.bases[1]=self.bases[0]
                self.bases[0]=self.battingTeam.currBatter
                result='FIELDER\'S CHOICE'
            elif x<96:
                self.outs+=1
                self.bases[2]=self.bases[1]
                self.bases[1]=self.bases[0]
                self.bases[0]=None
                result='GROUNDOUT'
            else:
                if self.bases[2]!=None:
                    self.score[self.battingTeamIndex]+=1
                    self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                    self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
                    self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
                self.bases[2]=self.bases[1]
                self.bases[1]=self.bases[0]
                self.bases[0]=self.battingTeam.currBatter
                self.errors[self.pitchingTeamIndex]+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS-=1
                result='ERROR'
        elif self.bases[2]==None and self.bases[1]!=None and self.bases[0]==None:
            x=random.randint(1,100)
            if x<50:
                self.outs+=1
                self.bases[2]=self.bases[1]
                self.bases[1]=self.bases[0]
                self.bases[0]=None
                result='GROUNDOUT'
            elif x<96:
                self.outs+=1
                result='GROUNDOUT'
            else:
                if self.bases[2]!=None:
                    self.score[self.battingTeamIndex]+=1
                    self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                    self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
                    self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
                self.bases[2]=self.bases[1]
                self.bases[1]=self.bases[0]
                self.bases[0]=self.battingTeam.currBatter
                self.errors[self.pitchingTeamIndex]+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS-=1
                result='ERROR'
        elif self.bases[2]==None and self.bases[1]==None and self.bases[0]!=None:
            x=random.randint(1,100)
            if x<20:
                self.outs+=2
                self.bases=[None,None,None]
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS+=1
                result='DOUBLE PLAY'
            elif x<60:
                self.outs+=1
                self.bases[1]=None
                self.bases[0]=self.battingTeam.currBatter
                result='FIELDER\'S CHOICE'
            elif x<96:
                self.outs+=1
                self.bases[1]=self.bases[0]
                self.bases[0]=None
                result='GROUNDOUT'
            else:
                if self.bases[2]!=None:
                    self.score[self.battingTeamIndex]+=1
                    self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                    self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
                    self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
                self.bases[2]=self.bases[1]
                self.bases[1]=self.bases[0]
                self.bases[0]=self.battingTeam.currBatter
                self.errors[self.pitchingTeamIndex]+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS-=1
                result='ERROR'
        elif self.bases[2]==None and self.bases[1]==None and self.bases[0]==None:
            x=random.randint(1,100)
            if x<96:
                self.outs+=1
                self.bases=[None,None,None]
                result='GROUNDOUT'
            else:
                if self.bases[2]!=None:
                    self.score[self.battingTeamIndex]+=1
                    self.inningScore[self.inning-1][self.battingTeamIndex]+=1
                    self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
                    self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
                self.bases[2]=self.bases[1]
                self.bases[1]=self.bases[0]
                self.bases[0]=self.battingTeam.currBatter
                self.errors[self.pitchingTeamIndex]+=1
                self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS-=1
                result='ERROR'
        self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].AB+=1
        self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS+=1
        self.changeBatter()
        self.checkGameStatus()
        if location=='3':
            return 'Y,-3.75,5,2,%s'%result
        elif location=='3S':
            return 'Y,-2.5,5,2,%s'%result
        elif location=='SS':
            return 'Y,-1.5,5,2,%s'%result
        elif location=='S2':
            return 'Y,0,8,2,%s'%result
        elif location=='2':
            return 'Y,1.5,5,2,%s'%result
        elif location=='21':
            return 'Y,2.5,5,2,%s'%result
        elif location=='1':
            return 'Y,4,5,2,%s'%result
        elif location=='Ca':
            return 'Y,.5,2,2,%s'%result
        elif location=='P':
            return 'Y,-.5,2,2,%s'%result
        else:
            return 'Y,3,5,2,%s'%result

    def strikeout(self):
        self.outs+=1
        self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].AB+=1
        self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].SO+=1
        self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].K+=1
        self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].OUTS+=1
        self.changeBatter()
        self.checkGameStatus()

    def walk(self):
        if self.bases[2]!=None and self.bases[1]!=None and self.bases[0]!=None:
            self.score[self.battingTeamIndex]+=1
            self.inningScore[self.inning-1][self.battingTeamIndex]+=1
            self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].RBI+=1
            self.battingTeam.inGamePlayers[self.bases[2].name].R+=1
            self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].RA+=1
            self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].ER+=1
            self.bases[2]=self.bases[1]
            self.bases[1]=self.bases[0]
            self.bases[0]=self.battingTeam.currBatter
        elif self.bases[0]==None:
            self.bases[0]=self.battingTeam.currBatter
        elif self.bases[2]==None and self.bases[1]!=None and self.bases[0]!=None:
            self.bases[2]=self.bases[1]
            self.bases[1]=self.bases[0]
            self.bases[0]=self.battingTeam.currBatter
        elif self.bases[2]==None and self.bases[1]==None and self.bases[0]!=None:
            self.bases[1]=self.bases[0]
            self.bases[0]=self.battingTeam.currBatter
        elif self.bases[2]!=None and self.bases[1]==None and self.bases[0]!=None:
            self.bases[1]=self.bases[0]
            self.bases[0]=self.battingTeam.currBatter
        self.battingTeam.inGamePlayers[self.battingTeam.currBatter.name].BB+=1
        self.pitchingTeam.inGamePlayers[self.pitchingTeam.currPitcher.name].BA+=1
        self.changeBatter()
        self.checkGameStatus()

class GameTeam(object):
    def __init__(self,team,dh,rotationLoc):
        self.team=team
        self.roster=self.team.roster
        self.inGamePlayers=dict()
        for name in self.roster.keys():
            player=self.roster[name]
            self.inGamePlayers[player.name]=GamePlayer(player)
        self.fielders=self.team.fielders
        self.pitchers=self.team.pitchers
        self.startingPitcher=self.team.rotation[rotationLoc]
        self.P=self.startingPitcher
        self.relievers=self.team.relievers
        if dh:
            self.lineup=[]
            for player in self.team.dhLineup:
                self.lineup.append(player[0])
                self.inGamePlayers[player[0].name]=GamePlayer(player[0],player[1])
                if player[1]=='C':
                    self.C=player
                elif player[1]=='1B':
                    self.fB=player
                elif player[1]=='2B':
                    self.sB=player
                elif player[1]=='3B':
                    self.tB=player
                elif player[1]=='SS':
                    self.SS=player
                elif player[1]=='LF':
                    self.LF=player
                elif player[1]=='CF':
                    self.CF=player
                elif player[1]=='RF':
                    self.RF=player
            self.bench=self.team.dhBench
        else:
            self.lineup=[]
            for player in self.team.normLineup:
                if player[0]!='Pitcher':
                    self.lineup.append(player[0])
                    self.inGamePlayers[player[0].name]=GamePlayer(player[0],player[1])
                else:
                    self.lineup.append(self.startingPitcher)
                    self.inGamePlayers[self.startingPitcher.name]=GamePlayer(self.startingPitcher,player[1])
                if player[1]=='C':
                    self.C=player
                elif player[1]=='1B':
                    self.fB=player
                elif player[1]=='2B':
                    self.sB=player
                elif player[1]=='3B':
                    self.tB=player
                elif player[1]=='SS':
                    self.SS=player
                elif player[1]=='LF':
                    self.LF=player
                elif player[1]=='CF':
                    self.CF=player
                elif player[1]=='RF':
                    self.RF=player
                elif player[1]=='DH':
                    self.DH=player
            self.bench=self.team.normBench
        self.index=0
        self.currPitcher=self.startingPitcher
        self.currBatter=self.lineup[self.index]
        self.pitchedPitchers=[]
        self.battedBatters=[]

    def checkPlayers(self):
        self.pitchedPitchers=[]
        self.battedBatters=[]
        for pitcher in self.pitchers:
            if self.inGamePlayers[pitcher.name].PC>0:
                self.pitchedPitchers.append(pitcher)
        for fielder in self.fielders:
            if self.inGamePlayers[fielder.name].AB>0:
                self.battedBatters.append(fielder)


class GamePlayer(object):
    def __init__(self,player,pos=None):
        self.name=player.name
        self.player=player
        if pos==None:
            self.gamePos=player.pos
        else:
            self.gamePos=pos
        self.AB=0
        self.H=0
        self.d=0
        self.t=0
        self.HR=0
        self.RBI=0
        self.R=0
        self.BB=0
        self.SO=0
        self.PC=0
        self.OUTS=0
        self.HA=0
        self.K=0
        self.BA=0
        self.RA=0
        self.ER=0
        self.HRA=0

    def getIP(self):
        self.IP=self.OUTS//3+.1*(self.OUTS%3)

    def __repr__(self):
        return self.name