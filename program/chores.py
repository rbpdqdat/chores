import pandas as pd
import numpy as np
import random

chore = pd.read_csv('../data/chores.csv',sep=',')
helpers = pd.read_csv('../data/helpers.csv',sep=',')

hCount = (helpers['helper'].count())

allchore = chore.query("randomAssigned == 'F'")
allchore.reset_index()
otherChore = chore.query("randomAssigned == 'T'")
otherChore.reset_index()
oChoreCount = otherChore['chore'].count()
sumChores = otherChore['weeklyFrequency'].sum()
chorePerHelper = sumChores/hCount

print(oChoreCount)
print(sumChores)
print(chorePerHelper)

t = {}

def addAllChores():
    k = [[] for i in range(7)]
    for index,row in allchore.iterrows():
        if row[1] == 7:
            for p in range(0,7):
                k[p].append(row[0])
        else:
            r = random.sample(range(7), k = row[1])
            for rnum in r:
            	k[rnum].append(row[0])
    return k

def addOtherChores(row):
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
            helpRandom = random.randint(0,helpersCount-1)
            wchore[i] = helperGroup['helper'][helpRandom]
    else:
        for i in dayOfChore:
            helpRandom = random.randint(0,helpersCount-1)
            wchore[i] = helperGroup['helper'][helpRandom]
    return wchore

for j in helpers['helper']:
    t[j] = addAllChores()

    #addOtherChores()
    #t[j].update(addOtherChores())

print(otherChore.apply(addOtherChores,axis=1))
