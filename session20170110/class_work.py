# Introduction to classes


class Employee:

    pay_increase = 1.05


    def __init__(self, first, last, pay):
        self.firstname = first
        self.lastname = last
        self.salary = pay
        self.email = "{0}.{1}@company.com".format(self.firstname, self.lastname)


    def full_details(self):
        full_details = "Full name - {0} {1}, email - {2}".format(self.firstname, self.lastname, self.email)
        return full_details


    def apply_pay_increase(self):
        return int(self.salary * self.pay_increase)

    # example of a class method
    @classmethod
    def modify_pay_rate(cls):
        cls.pay_increase = 1.08

    # example of a static method
    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


class Developer(Employee):

    pay_increase = 1.1 # Developers have a higher pay rate

    def __init__(self, first, last, pay, lang):
        Employee.__init__(self, first, last, pay)
        self.language = lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self, first, last, pay) # for python3 use super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees


    # Function to add employees
    def add_employees(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            print("You already manage this employee")


    # function to remove employees
    def remove_employees(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            print("You do not manage this employee")


    def print_employees(self):
        for emp in self.employees:
            print("--- ", emp)

