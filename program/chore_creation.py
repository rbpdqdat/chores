import pandas as pd
import numpy as np
import random
import json
from chore_assist import chore
from chore_assist import helper
from chore_assist import choreChart


chore = pd.read_csv('../data/chore_list.csv',sep=',')
chore.sort_values('day_of_week', ascending=True, inplace=True)
#dropping all unassigned chores
chore = chore[chore.assigned != 'F' ]
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
    if row['Assigned'] == 'T':
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
            for d in dayOfChore:
                if row['randomAssigned'] == 'T':
                    helpRandom = random.randint(0,helpersCount-1)
                    wchore[d] = helperGroup['helper'][helpRandom]
                else:
                    wchore[d] = [h for h in helperGroup['helper']]
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
                jCount+=1
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

for worker in helperChart:
    f = open('../output/'+worker+".html", "w")
    f.write('<!DOCTYPE html><html><head><meta charset="UTF-8"></head><body><b><font size = "4">'+
            worker + " Duties</font></b><table border=1><thead><tr><th>Sunday</th><th>Monday</th><th>Tuesday</th><th>Wednesday</th><th>Thursday</th><th>Friday</th><th>Saturday</th></tr></thead><tbody><tr>")
    for daytasks in helperChart[worker]:
        f.write('<td>')
        for task in daytasks:
            f.write('<p><input id="checkBox" type="checkbox"> '+task+'</p>')
        f.write('</td>')
    f.write('</tr></tbody></table></body></html>')
    f.close()
#json_string = json.dumps(helperChart)
#with open('../output/chore.json', 'w') as outfile:
#        json.dump(json_string, outfile)
