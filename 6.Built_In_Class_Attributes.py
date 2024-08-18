class Employee:
    """this is the Employee Class for maintaining employee DAta"""
    def __init__(self, sal, ag):
        self.salary = sal
        self.age = ag

    def display(self):
        print(f"salary is {self.salary} and age is {self.age}")


e1 = Employee(24000, 2)
e2 = Employee(26000, 26)
e3 = Employee(30000, 78)


print(Employee.__doc__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
