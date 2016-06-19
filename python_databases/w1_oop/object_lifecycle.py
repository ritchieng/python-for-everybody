# ONE INSTANCE EXAMPLE ALONG WITH CONSTRUCTOR
class PartyAnimal:
    # One instance here
    x = 0

    # Double underscores, methods when something happens
    # When constructor runs, this happens
    def __init__(self):
        print "I am constructed"

    def party(self):
        self.x = self.x + 1
        print 'So far', self.x

    def __del__(self):
        print 'I am destructed', self.x

an = PartyAnimal()

an.party()
an.party()
an.party()

# TWO INSTANCE VARIABLE
class PartyAnimal2:
    # 1st instance variable
    x = 0
    # 2nd instance variable
    name = ''

    # constructor 2 params
    # self: alias of instance we're in
    # nam: name param
    def __init__(self, nam):
        self.name = nam
        print self.name, 'constructed'

    # Self becomes an alias for s or j
    def party(self):
        self.x = self.x + 1
        print self.name, 'party count', self.x

s = PartyAnimal2('Sally')
# Short-form of PartyAnimal2.party(s)
s.party()

j = PartyAnimal2('Jim')
# Short-form of PartyAnimal2.party(j)
j.party()
s.party()