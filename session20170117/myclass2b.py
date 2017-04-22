class Shape:
    
    colour = 'red'
    
    def __init__(self,type):
        self.type = type
        
    def about(self):
        desc = 'This is a {0} {1}'.format(Shape.colour, self.type)
        print(desc)
        
        
sh1 = Shape('circle')
sh1.about()

sh2 = Shape('triangle')
sh2.about()