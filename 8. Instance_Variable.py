"""

"""

class Employee:
    def __init__(self, sal, ag):
        self.salary = sal #instance variables
        self.age = ag # instance Variables

    def display(self):
        print(f"salary is {self.salary} and age is {self.age}")

    def change_data(self):
        self.salary = int(input("Enter the salary: "))
        self.age = int(input("Enter the age: "))

e1 = Employee(24000, 2)
e2 = Employee(26000, 26)
e3 = Employee(30000, 78)


e1.name="Test" # instance variable for e1 object
print(e1.__dict__)

e2. change_data()
print(e2.__dict__)