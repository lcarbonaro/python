class Shape:

    def __init__(self,type):
        self.type = type
        
    def about(self):
        desc = 'This is a {0}'.format(self.type)
        print(desc)
        
        
sh1 = Shape('circle')
sh1.about()
