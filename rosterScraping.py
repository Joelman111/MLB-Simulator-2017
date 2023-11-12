import requests
import sys
import string
from bs4 import BeautifulSoup

def writeFile(path, contents):
    with open(path, 'w') as f:
        f.write(contents)


url='http://bleacherreport.com/articles/2696277-updated-spring-training-predictions-for-all-30-mlb-teams-final-25-man-rosters'
r=requests.get(url)
soup=BeautifulSoup(r.content,'html.parser')


gdata=soup.find_all('div',{'class':'atom table'})

result=[]
for item in gdata:
    nameData=item.find_all('td')
    for name in nameData:
        x=name.text
        x=x.replace(u'\xa0','')
        if x=='Starters' or x=='Bench' or x=='' or x=='Rotation' or x=='Bullpen':
            pass
        else:
            for pos in ['OF/DH ','C/OF/P ','1B/OF ','1B/DH ','INF/OF ','C/OF ','C ','1B ','2B ','OF ','INF ','3B ','SS ','LF ','CF ','RF ','RHP ','LHP ','F ', 'DH ']:
                if pos in x:
                    if ('JC Ramirez' in x or 'Sabathia' in x) and pos=='C ':
                        pass
                    else:
                        x=x.replace(pos,'',1)
            x=x.strip()
            result.append(x)

# for num,team in enumerate(['ARZ','ATL','BAL','BOS','CHC', 'CHW', 'CIN','CLE','COL','DET','HOU','KC','LAA','LAD','MIA','MIL','MIN','NYM','NYY','OAK','PHI','PIT','STL','SDP','SFG','SEA','TB','TEX','TOR','WSH']):
#     content=''
#     for i in range(25):
#         player=num*25+i
#         content+=result[player]+'\n'
#     print(content)