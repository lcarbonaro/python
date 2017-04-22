class Shape():
    
    colour = "red"
    
    def __init__(self, type):
        self.type = type
        
    def show(self):
        desc = "This is a {0} {1}".format(Shape.colour,self.type)
        print(desc)
        
    @classmethod
    def set_colour(cls, colour):
        cls.colour = colour
    
    @staticmethod
    def convert_to_cm(inches):
        result = "{0} in = {1} cm".format(inches,inches*2.5)
        print(result)

        
sh1 = Shape("circle")
sh1.show()        

sh1.convert_to_cm(2)

Shape.set_colour("blue")

sh2 = Shape("triangle")
sh2.show() 