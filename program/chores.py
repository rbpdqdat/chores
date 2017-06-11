import pandas as pd
import numpy as np
import random

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
ch = []

#for key in chartDict:
    #if type(chartDict[key]) == type(list):
    #    for j in chartDict[key]:
    #        for name in j:
    #            print(j.index())
    #            print(key)
    #            helperChart[name].update(ch[j.index()].append(key))
    #else:
    #     helperChart[chartDict[key]].update(ch[j.index()].append(key))

#print(helperChart)
