import pandas as pd
import numpy as np
import random
import json

chore = pd.read_csv('../data/chores.csv',sep=',')
chore.sort_values('randomAssigned', ascending=True, inplace=True)
helpers = pd.read_csv('../data/helpers.csv',sep=',')

hCount = (helpers['helper'].count())

choreCount = chore['chore'].count()
sumChores = chore['weeklyFrequency'].sum()
chorePerHelper = sumChores/hCount

print(choreCount)
print(sumChores)
print(chorePerHelper)
chartDict = {}

def choreAssign(row):
    dayOfChore = random.sample(range(7), k = row['weeklyFrequency'])
    minAge = row['minAge']
    c = row['chore']
    helperGroup = helpers.query('age >= @minAge')
    helperGroup.reset_index()
    helpersCount = helperGroup['age'].count()
    wchore = [[] for i in range(7)]
    if row['dayofWeek'] != '*':
        rsplit = row['dayofWeek'].split(';')
        for dChore in rsplit:
            helpRandom = random.randint(0,helpersCount-1)
            dChore = int(dChore)
            wchore[dChore] = helperGroup['helper'][helpRandom]  
    elif row['weeklyFrequency'] == 7:
        for i in range(7):
            if row['randomAssigned'] == 'T':
                helpRandom = random.randint(0,helpersCount-1)
                wchore[i] = helperGroup['helper'][helpRandom]
            else:
                wchore[i] = [h for h in helperGroup['helper']]
    else:
        for i in dayOfChore:
            if row['randomAssigned'] == 'T':
                helpRandom = random.randint(0,helpersCount-1)
                wchore[i] = helperGroup['helper'][helpRandom]
            else:
                wchore[i] = [h for h in helperGroup['helper']]
    chartDict[row['chore']] = wchore

    return 

chore.apply(choreAssign,axis=1)
helperChart = {}

def createHelperChart(helperName):
    hname = [[] for i in range(7)]
    #charDict[key] is a list of lists
    for key in chartDict:
        #jCount is the day of the week
        jCount = 0
        for j in chartDict[key]:
            if not j: 
                continue
            else:
                if len(j) >1 :
                    if (isinstance(j,str)):
                        if j == helperName:
                            hname[jCount].append(key)
                    else:
                        for name in j:
                            if name == helperName:
                                hname[jCount].append(key)
            jCount += 1
    return hname

for hChore in helpers['helper']:
    helperChart[hChore] = createHelperChart(hChore)

json_string = json.dumps(helperChart)
with open('chore.json', 'w') as outfile:
        json.dump(json_string, outfile)
