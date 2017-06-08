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

def addOtherChores():
    dayOfChore = random.sample(range(7), k = otherChore['weeklyFrequency'])
    minAge = otherChore['minAge']
    if otherChore['dayofWeek'] != '*':
        for dayOfChore in otherChore['dayofWeek'].split(';'):
            helperGroup = helpers.query("age >= @minAge")

for j in helpers['helper']:
    t[j] = addAllChores()
    #addOtherChores()
    #t[j].update(addOtherChores())

print(t)
