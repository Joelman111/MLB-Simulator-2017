import os

def readFile(path):
    with open(path, 'r') as f:
        return f.read()

def writeFile(path, contents):
    with open(path, 'w') as f:
        f.write(contents)
        
contents=''
for file in os.listdir('Real Rosters'):
    roster=readFile('Real Rosters\\%s'%file)
    for player in roster.splitlines():
        contents+='Player: '+player+'\n'
        contents+='Num: '+str(20)+'\n'
        contents+='Pos: '+'C'+'\n'
        contents+='Rat: '+'75,75,75,75,75,75'+'\n'+'\n'
writeFile('MLB Players Old.txt',contents)