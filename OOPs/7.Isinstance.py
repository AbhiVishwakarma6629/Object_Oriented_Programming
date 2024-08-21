class Demo:
    pass

class Employee:
    def __init__(self, sal, ag):
        self.salary = sal
        self.age = ag

    def display(self):
        print(f"salary is {self.salary} and age is {self.age}")


e1 = Employee(24000, 2)
e2 = Employee(26000, 26)
e3 = Employee(30000, 78)

if isinstance(e1, Demo):
    print("True")
else:
    print("False")