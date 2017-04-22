class Animal:
    
    def __init__(self,species,food):
        self.species = species
        self.food = food
    
    def about(self):
        desc = 'I am a {0}. I like to eat {1}.'.format(self.species,self.food)
        print(desc)
        
class Pet(Animal):
    
    def __init__(self,species,food,name,human):
        Animal.__init__(self,species,food)
        self.name = name
        self.human = human
        
    def intro(self):
        who = 'I am {0} and my human is {1}.'.format(self.name,self.human)
        print(who)


pet1 = Pet('cat', 'tuna', 'Fluffy', 'Tom')
pet1.about()
pet1.intro()
