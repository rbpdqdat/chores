import numpy as np

class Chore:
    'Defining chore object'

    #creating a running chore count based on frequency and helpers
    chore_count = 0
    def __init__(self, name, frequency, min_age, assigned_to, \
             day_of_week = '*'):
        self.name = name
        self.frequency = frequency
        self.day_of_week = day_of_week.split(';')
        self.min_age = min_age
        self.assigned_to = assigned_to.split(';')

    def assign_chore(self):
        '''assigning chore and adding count'''
        Chore.chore_count += self.frequency * len(self.assigned_to)
        #for i in self.assigned_to:
        #    print(getattr(i, 'name', None))
        

    @classmethod
    def how_many(cls):
        print("{:d} of chores assigned.\n".format(cls.chore_count))


class Person:
    '''defining Person object'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Adult(Person):
    '''defining Adult subclass'''
    def __init__(self, name, age):
        Person.__init__(self, name, age)
        self.weekchart = np.empty([7,7], dtype=object)

class Child(Person):
    '''defining Child subclass'''
    def __init__(self, name, age):
        Person.__init__(self, name, age)
        self.reward = age * 0.5
        print('Initialized Child {}'.format(self.name))
        self.weekchart = np.empty([7,7],dtype=object)
        self.day_of_ct = [0 for i in range(7)]
        self.chore = ''
        self.day_of_week = ''
    def add_chore(self,chore,day_of_week):
        self.day_of_week = day_of_week
        self.chore = chore
        self.weekchart[[self.day_of_week],self.day_of_ct[day_of_week]] = self.chore
        self.day_of_ct[day_of_week] += 1
        print('{} got {} as a chore'.format(self.name,self.chore))


import pandas as pd

#helpers = pd.read_csv('../data/helpers.csv',sep=',')
f = open('../data/helpers.csv')
#skip header
lines = f.readlines()[1:]
f.close()

listofchores = open('../data/chore_list.csv')
#choreheader = listofchores.readlines()[0]
chorelines = listofchores.readlines()[1:]
listofchores.close()

def helperList(minimum_age,hlist):
    helpernames = []
    for helpers in hlist:
        if helpers[1] >= minimum_age
            helpernames.append(helpers[0])
    return helpernames

for choreline in chorelines:
    choreline = choreline.replace('\n')
    work,frequency,min_age,assigned_to,assigned,day_of_week = choreline.split(',')  
    assigned_to = assigned_to.split(';')
    day_of_week = day_of_week.split(';')
    if assigned_to == '*': 
        available_helpers = helperList(min_age, lines)
    else:
        available_helpers = assigned_to
    

Devin = Child('Devin',9)
Lyndon = Child('Lyndon',7)
Sam = Child('Sam',4)

Devin.add_chore('sweep',0)


print(Devin.weekchart)




