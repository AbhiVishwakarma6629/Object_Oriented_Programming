"""
1. getattr(object_name, attribute_name)
2. setattr(object_name, attribute_name, new_value)
3. delattr(object_name, attribute_name)
4. hasattr(object_name, attribute_name)
"""

class Employee:
    def __init__(self, sal, ag):
        self.salary = sal
        self.age = ag

    def display(self):
        print(f"salary is {self.salary} and age is {self.age}")


e1 = Employee(24000, 2)
e2 = Employee(26000, 26)
e3 = Employee(30000, 78)

print(getattr(e1, 'age'))
setattr(e2, 'age', 30)
print(getattr(e2, 'age'))

delattr(e3, 'age')
print(e3, 'age')

print(hasattr(e3, 'age'))