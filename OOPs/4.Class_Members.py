"""
1. Class Members :- Attributes(variables) + Actions(Methods)
2. we can access these variables using object outside the class.
3.syntax :-
    -> Accessing attributes:- object_name.variable_name
    -> Accessing Methods:- object_name.method_name(
"""


class Employee:
    def __init__(self, sal, ag):
        self.salary = sal
        self.age = ag

    def display(self):
        print(f"salary is {self.salary} and age is {self.age}")


e1 = Employee(24000, 2)
e2 = Employee(26000, 26)

# accessing the attributes outside the class
print(e1.salary)
e1.salary = 34000

print(e2.age)
print(e1.display())
