class Employee:
    
    payIncRate = 1.05
    
    def __init__(self,first, last, pay):
        self.firstName = first
        self.lastName = last
        self.salary = pay
        self.email = self.firstName + "." + self.lastName + "@company.com"
        
    def fullDetails(self):
        fd = "My is name is {0} and my salary is ${1}".format(self.firstName,self.salary)
        return fd

    def newPay(self):
        return self.salary * self.payIncRate
        
    @classmethod
    def modifyPayIncRate(cls):
        cls.payIncRate = 1.08

    @staticmethod
    def someFunc():
        pass

# inheritance
class Developer(Employee):
    
    def __init__(self,first,last,pay, lang):
        Employee.__init__(self, first,last,pay)
        self.language = lang
        

dev1 = Developer("Jack","Spratt",10000,"JS")
print(dev1.email)

#create add employee to manager
#remove employee to manager



emp1 = Employee("Tom","Jones",50000)
print(emp1.email)
print(emp1.fullDetails())

emp2 = Employee("Jane", "Doe", 55000)

print( emp1.newPay() )
print(emp2.newPay())

