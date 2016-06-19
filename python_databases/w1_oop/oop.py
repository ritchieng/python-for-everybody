# PartyAnimal: class for making PartyAnimal objects
class PartyAnimal:
    # x = 0: each PartyAnimal object has data
    x = 0

    # def: each PartyAnimal object has code
    # every method must have >= 1 parameters
    def party(self):
        self.x = self.x + 1
        print 'So far', self.x

# Create PartyAnimal object/instance
an = PartyAnimal()
# an would have
# data: x = 0
# code: party()
print type(an)
print dir(an)

# Call party() method
# Short-form of PartyAnimal.party(an)
an.party()
# self is an alias of an
# data: x = 0 + 1 = 1
# code: party()
an.party()
# data: x = 1 + 1 = 2
# code: party()
an.party()
# data: x = 2 + 1 = 3
# code: party()

a = list()
# list() is built-in class

type(a)

print dir(a)
# methods: operations that the object can perform
# append()
# pop()