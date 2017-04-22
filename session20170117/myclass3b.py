class Shape:
    
    colour = 'red'
    
    def __init__(self,type):
        self.type = type
        
    def about(self):
        desc = 'This is a {0} {1}'.format(Shape.colour, self.type)
        print(desc)
    
    @classmethod
    def set_colour(cls, new_colour):
        cls.colour = new_colour
        
    @staticmethod
    def convert_to_cm(inches):
        return '{0} ins. = {1} cm'.format(inches, inches * 2.5) 
        
sh1 = Shape('circle')
sh1.about()

Shape.set_colour('blue')

sh2 = Shape('triangle')
sh2.about()

print(Shape.convert_to_cm(3))
