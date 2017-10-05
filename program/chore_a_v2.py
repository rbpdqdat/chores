import numpy as np
import datetime
import random

class Person:
    '''defining Person object'''
    def __init__(self, name, age):
        self.name = name
        self.age = None
        self.weekchart = np.empty([7,7],dtype=object)
        self.day_of_ct = [0 for i in range(7)]
        self.chore = ''
        self.day_of_week = ''
    def add_chore(self,chore,day_of_week):
        '''add_chore method in class 
           add chores to the 7 X 7 matrix'''
        self.day_of_week = day_of_week
        self.chore = chore
        self.weekchart[[self.day_of_week],self.day_of_ct[day_of_week]] = self.chore
        self.day_of_ct[day_of_week] += 1
        print('{} got {} as a chore on day {}'.format(self.name,self.chore,self.day_of_week))

class Adult(Person):
    '''defining Adult by inheriting attributes from Person class'''
    def __init__(self, name, age):
        Person.__init__(self, name, age)

class Child(Person):
    '''defining Child subclass'''
    def __init__(self, name, age):
        '''defining Clss by inheriting attributes from Person class'''
        Person.__init__(self, name, age)
        self.reward = age * 0.5

class Chore:
    '''Define the Chore class'''
    def __init__(self,chore,freq,age_require,delegate,due,day,qt):
        self.chore = chore
        self.freq = freq
        self.age_require = age_require
        self.delegate = delegate.split(';')
        self.due = due
        self.day = day.split(';')
        self.qt = qt



#helpers = pd.read_csv('../data/helpers.csv',sep=',')
f = open('../data/helpers.csv')
#skip header
lines = f.readlines()[1:]
f.close()

listofchores = open('../data/chore_list.csv')
#choreheader = listofchores.readlines()[0]
#skip first row/header
chorelines = listofchores.readlines()[1:]
listofchores.close()

#read in helpers and ages from 'helpers.csv'
def helperList(minimum_age,hlist):
    helpernames = []
    for helpers in hlist:
        helpers = helpers.replace('\n','')
        helper,age = helpers.split(',')
        age = int(age)
        minimum_age = int(minimum_age)
        if age >= minimum_age:
            helpernames.append(helper)
    return helpernames
    
def workerpick(helpgroup):
    #print(helpgroup)
    x = [random.choice(helpgroup)]
    return x

#This is where a class is useful
#daylist needs to be tracked as a general method for each
#chore
def assignchore(work,worker,chorenumber,daylist,day_of_week):
    print(work,worker,chorenumber,daylist,day_of_week)
    if day_of_week == '*':
        dayofchore = random.choice(daylist)
    else:
        dayofchore = day_of_week[chorenumber]
    daychore = int(dayofchore)
    print(type(dayofchore))    
    if worker == 'Devin':
        # I would like to reinput the chore into the randomization
        #scheme if one of the days is filled over the max number of chores
        if (Devin.day_of_ct[daychore]) <= 7:
            Devin.add_chore(work,daychore)
    if worker == 'Lyndon':
        if (Lyndon.day_of_ct[daychore]) <= 7:
            Lyndon.add_chore(work,daychore)
    if worker == 'Sam':
        if (Lyndon.day_of_ct[daychore]) <= 7:
            Sam.add_chore(work,daychore)
    if day_of_week == '*':
        daylist = daylist.remove(dayofchore)

    return 



Devin = Child('Devin',9)
Lyndon = Child('Lyndon',7)
Sam = Child('Sam',4)

#read in chores from chore list
for choreline in chorelines:
    choreline = choreline.replace('\n','')
    work,weekly_freq,min_age,assigned_to,day_of_week = choreline.split(',')
    if assigned_to == None:
        pass
    else: 
        weekly_freq = int(weekly_freq)
        qty = weekly_freq * len(assigned_to.split(';'))

    # assigned_to = '*' means random assignemt given age restrictions
        #assigned_to = assigned_to.split(';')
    #daylist is used for random assignemnt
        daylist = [i for i in range(0,7)]
        if day_of_week != '*':
            day_of_week = day_of_week.split(';')
    #chorenumber is really the number of times a chore will be done each week
    #!!!!!!!!!
    #chorenumber can't be reliably used to index the daylist
    #!!!!!!!!!
        for chorenumber in range(weekly_freq):
            print(work,weekly_freq,chorenumber,assigned_to,day_of_week)
            if assigned_to == '*':
                worker = workerpick(helperList(min_age, lines))
                assignchore(work,worker,chorenumber,daylist,day_of_week)
            else:
                for worker in assigned_to.split(';'):
                    assignchore(work,worker,chorenumber,daylist,day_of_week)
            # the single entity word is being split by letter

    # weekly frequency - day_of_week - available_helpers interaction
    # if assigned_to == '*' then 

Devin.name

f = open('../output/'+Devin.name+"1.html", "w")
f.write('<!DOCTYPE html><html><head><meta charset="UTF-8"></head><body><b><font size = "4">'+
      Devin.name + " Duties</font></b><table border=1><thead><tr><th>Sunday</th><th>Monday</th><th>Tuesday</th><th>Wednesday</th><th>Thursday</th><th>Friday</th><th>Saturday</th></tr></thead><tbody><tr>")
for daytasks in Devin.weekchart:
    f.write('<td>')
    for task in daytasks:
        if task != None:
            f.write('<p><input id="checkBox" type="checkbox"> '+task+'</p>')
    f.write('</td>')
f.write('</tr></tbody></table></body></html>')
f.close()

print(Devin.weekchart)
print(Lyndon.weekchart)
print(Sam.weekchart)




