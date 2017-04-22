class Shape:
    
    colour = 'red'
    
    def __init__(self,type):
        self.type = type
        
    def about(self):
        desc = 'This is a {0} {1}'.format(Shape.colour, self.type)
        print(desc)
    
    @classmethod
    def setColour(cls, new_colour):
        cls.colour = new_colour
        
sh1 = Shape('circle')
sh1.about()

Shape.setColour('blue')

sh2 = Shape('triangle')
sh2.about()
