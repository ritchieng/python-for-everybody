class PartyAnimal:
    # Two INSTANCES/VARIABLES here
    x = 0
    name = ''

    # CONSTRUCTOR
    # Double underscores, methods when something happens
    # When constructor runs, this happens
    # constructor 2 params
    # self: alias of instance we're in
    # nam: name param
    def __init__(self, nam):
        self.name = nam
        print self.name, 'constructed'

    # Self becomes an alias for s or j
    def party(self):
        self.x += 1
        print self.name, 'party count', self.x

# FootballFan is a class that extends PartyAnimal
# All the capabilities of PartyAnimal and more
class FootballFan(PartyAnimal):
    # Add new variable/
    points = 0

    # Add one new method
    def touchdown(self):
        self.points += 7
        self.party()
        print self.name, 'points', self.points

# Create PartyAnimal object/instance
s = PartyAnimal('Sally')
# short-form is s.party()
PartyAnimal.party(s)

# Create FootballFan object/instance
j = FootballFan('Jim')
# short-form is j.party()
FootballFan.party(j)

# short-form is j.touchdown()
FootballFan.touchdown(j)

# 3 OBJECTS/INSTANCES in total
# x, name and points
