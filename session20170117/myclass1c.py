class Animal:
    
    def __init__(self,species,food):
        self.species = species
        self.food = food
    
    def about(self):
        desc = 'I am a {0}. I like to eat {1}'.format(self.species,self.food)
        print(desc)
        
an1 = Animal('dog','meat')
an1.about()

an2 = Animal('horse','hay')
an2.about()
