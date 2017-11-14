class chore:
    'Defining chore object'
    def __init__(self, name, frequency, min_age, assigned_to, \
            assigned = False, random_assigned = False, day_of_week = '*'):
        self.name = name
        self.frequency = frequency
        self.day_of_week = day_of_week
        self.min_age = min_age
        self.assigned_to = assignedto
        self.assigned = assigned
        self.random_assigned = random_assigned

class helper:
    ' Defining the helper object'
    def __init__(self, name, age, max_chores = 5):
        self.name = name
        self.age = age
        self.max_chores = max_chores


class adult(Helper):
    def __init__(self, name, age):
        pass

class child(Helper):
    def __init__(self, name, age):
        pass

class choreChart:
    ' choreChart represents the empty 7X7 numpy matrix'
    def __init__(self, name):
        self.name = name
        self.weekchart = np.empty([7,7],dtype=object)