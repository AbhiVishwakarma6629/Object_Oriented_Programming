class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name of the Employee is {self.name} and age is {self.age}")


e1 = Employee('Raj', 21)
e2 = Employee('Jay', 22)

print(e1.display())
print(e2.display())