class Animal():
    
    def __init__(self, species, food):
        self.species = species
        self.food = food
        
    
    def desc(self):
        desc = "I am a {0} and I eat {1}".format(self.species, self.food)
        print(desc)
        

class Pet(Animal):
    
    def __init__(self, species, food, name, owner):
        Animal.__init__(self, species,food)
        self.name = name
        self.owner = owner
        
    def intro(self):
        desc = "My name is {0} and my owner is {1}".format(self.name, self.owner)
        print(desc)
        
an1 = Animal("lion","meat")
an1.desc()

an2= Animal("koala","eucalyptus")
an2.desc()

pet = Pet("cat","tuna", "Bertie", "Tom")
pet.desc()
pet.intro()