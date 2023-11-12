import requests
import random
import math
import os
from bs4 import BeautifulSoup

def writeFile(path, contents):
    with open(path, 'w') as f:
        f.write(contents)

def readFile(path):
    with open(path, 'r') as f:
        return f.read()

def getBattingStats(players):
    urlB='http://mlb.mlb.com/pubajax/wf/flow/stats.splayer?season=2016&sort_order=%%27desc%27&sort_column=%%27ab%27&stat_type=hitting&page_type=SortablePlayer&game_type=%27R%27&player_pool=ALL&season_type=ANY&sport_code=%27mlb%27&results=1000&recSP=1&recPP=1266'
    urlF='http://mlb.mlb.com/pubajax/wf/flow/stats.splayer?season=2016&sort_order=%%27desc%27&sort_column=%%27inn%27&stat_type=fielding&page_type=SortablePlayer&game_type=%27R%27&player_pool=ALL&season_type=ANY&sport_code=%27mlb%27&results=1000&recSP=1&recPP=1266'
    urlP='http://mlb.mlb.com/pubajax/wf/flow/stats.splayer?season=2016&sort_order=%%27desc%27&sort_column=%%27g%27&stat_type=pitching&page_type=SortablePlayer&game_type=%27R%27&player_pool=ALL&season_type=ANY&sport_code=%27mlb%27&results=1000&position=%%271%%27&recSP=1&recPP=1266'
    rB=requests.get(urlB)
    rF=requests.get(urlF)
    rP=requests.get(urlP)
    bStatsDict=eval(rB.content)
    fStatsDict=eval(rF.content)
    pStatsDict=eval(rP.content)
    battingStats=bStatsDict['stats_sortable_player']['queryResults']['row']
    fieldingStats=fStatsDict['stats_sortable_player']['queryResults']['row']
    pitchingStats=pStatsDict['stats_sortable_player']['queryResults']['row']
    contents=''
    createdPlayers=[]
    for i,player in enumerate(battingStats):
        if player['name_display_first_last'] in players.keys() and int(player['tpa'])>=100:
            #print(i,player['name_display_first_last'])
            contents+='Player: '+player['name_display_first_last']+'\n'
            createdPlayers.append(player['name_display_first_last'])
            contents+='Pos: '+player['pos']+'\n'
            contents+='Num: '+player['jersey_number']+'\n'
            #print(player['name_display_first_last'])
            battingRatings=createBattingRatings(float(player['avg']),int(player['tpa']),float(player['ops']),int(player['so']),float(player['obp']),float(player['slg']),int(player['hr']),int(player['bb']),int(player['sb']),int(player['d']),int(player['t']))
            try:
                index=fielderIndex(fieldingStats,player)
                fieldingRating=createFieldingRating(float(fieldingStats[index]['fpct']))
            except:
                fieldingRating=75
            ovr=round(.3*battingRatings[0]+.25*battingRatings[1]+.25*battingRatings[2]+.12*battingRatings[3]+.08*fieldingRating)
            ratings=''
            ratings+=str(ovr)
            ratings+=','
            for rating in battingRatings:
                ratings+=str(rating)+','
            ratings+=str(fieldingRating)
            contents+='Rat: '+ratings+'\n'+'\n'
    for i,player in enumerate(pitchingStats):
        if player['name_display_first_last'] in players.keys() and int(player['g'])>=10:
            #print(i,player['name_display_first_last'])
            contents+='Player: '+player['name_display_first_last']+'\n'
            createdPlayers.append(player['name_display_first_last'])
            for file in os.listdir('assets\\teamData\\startingRotations'):
                starters=readFile('assets\\teamData\\startingRotations\\%s'%file)
                if player['name_display_first_last'] in starters:
                    contents+='Pos: SP'+'\n'
                    break
            if contents[-3:]!='SP\n':
                contents+='Pos: RP'+'\n'
            contents+='Num: '+player['jersey_number']+'\n'
            pitchingRatings=createPitchingRatings(float(player['era']),float(player['whip']),float(player['k_9']),float(player['bb_9']),float(player['hr']),float(player['avg']),float(player['slg']),float(player['ip']),int(player['g']),int(player['cg']))
            ovr=round(.35*pitchingRatings[0]+.25*pitchingRatings[1]+.3*pitchingRatings[3]+.1*pitchingRatings[4])
            ratings=''
            ratings+=str(ovr)
            ratings+=','
            for i in range(len(pitchingRatings)):
                if i!=4:
                    ratings+=str(pitchingRatings[i])+','
                else:
                    ratings+=str(pitchingRatings[i])
            contents+='Rat: '+ratings+'\n'+'\n'
    for i,player in enumerate(players.keys()):
        if player in createdPlayers:
            pass
        else:
            #print(i,player)
            contents+='Player: '+player+'\n'
            contents+='Pos: '+'\n'
            contents+='Num: '+str(random.randint(1,100))+'\n'
            contents+='Rat: 75,75,75,75,75,75'+'\n'+'\n'
            
    contents+='\n\nend'
    writeFile('assets\\playerData\\Player Ratings.txt',contents)

def createBattingRatings(avg,pa,ops,so,obp,slg,hr,bb,sb,d,t):
    so=so/pa*550
    hr=hr/pa*550
    bb=bb/pa*550
    sb=sb/pa*550
    d=d/pa*550
    t=t/pa*550
    con,pwr,dsp,spd=None,None,None,None
    con=round(.59*(225*pa**.05*avg)+.23*(82.5*pa**.05-.35*so)+.18*(74.5/(ops**.2)*pa**.05*ops))
    pwr=round(.49*(114.5*(slg*pa**.05)**.66)+.33*(50+3.5*(hr*pa**.05)**.68)+.18*(74.5/(ops**.2)*pa**.05*ops))
    dsp=round(.54*(18.204*(bb*pa**.05)**.35)+.28*(187.045*(obp*pa**.05)**1.06)+.18*(74.5/(ops**.2)*pa**.05*ops))
    spd=round(45+.7*(sb**.5*8)+.3*(t**.3*28))
    return min(100,con),min(100,pwr),min(100,dsp),min(100,spd)

def createPitchingRatings(era,whip,k_9,bb_9,hr,avg,slg,ip,g,cg):
    if bb_9!=0: k_bb=k_9/bb_9
    else: k_bb=10
    if hr!=0:   hr_9=hr/ip*9
    else:   hr_9=.5
    if era==0:
        era=1
    ctr,mov,stm,con,pwr=None,None,None,None,None
    ctr=round(.3*(112*(ip**.05/era)**.35)+.25*(77*(ip**.05/whip)**.7)+.45*(55*(ip**.05*k_bb)**.27))
    mov=round(.35*(112*(ip**.05/era)**.35)+.65*(6.8*(k_9*ip**.05)**1.05))
    stm=round(7.9*(ip/g+1)**1.2+2*cg)
    con=round(.25*(112*(ip**.05/era)**.35)+.75*(10.5*(ip**.05/avg)**1.2))
    pwr=round(.25*(112*(ip**.05/era)**.35)+.4*(500*(ip**.05/(hr_9+3.5))**1.5)+.35*(29*(ip**.05/slg)**.75))
    return min(100,ctr),min(100,mov),min(100,stm),min(100,con),min(100,pwr)

def createFieldingRating(fpct):
    return round(75+math.log(fpct/.97)*2000)

def fielderIndex(fieldingStats,player):
    for i in range(442):
        if fieldingStats[i]['name_display_first_last']==player:
            return i
    return None