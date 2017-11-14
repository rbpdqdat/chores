class Chore:
    '''Defining chore objects '''
    
    def __init__(self, name, frequency, min_age, assignedTo, \
            assigned = False, randomAssigned = False, day_of_week = '*'):
        self.name = name
        self.frequency = frequency
        self.day_of_week = day_of_week
        self.min_age = min_age
        self.assignedTo = assignedTo
        self.assigned = assigned
        self.randomAssigned = randomAssigned

class Helper:

    def __init__(self, name, age, max_chores = 5):
        self.name = name
        self.age = age
        self.max_chores = max_chores


class Adult(Helper):
    def __init__(self, name, age):
        pass

class Child(Helper):
    def __init__(self, name, age):
        pass
