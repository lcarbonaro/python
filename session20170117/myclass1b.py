class Animal:
    
    def about(self):
        desc = 'I am an animal'
        print(desc)
        
an1 = Animal()
an1.about()

an1.species = 'dog'
an1.food = 'meat'

an2 = Animal()
an2.about()

an2.species = 'horse'
an2.food = 'hay'