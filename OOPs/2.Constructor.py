# Special Methods used for initializing objects with attributes
# it is __init__() method
# First Argument is 'self'

"""
Types of Constructor
-> Default
-> Non Parametrized
-> Parametrized
"""


# default
class Employee:
    pass


e1 = Employee()
print(e1.__dict__)


# Non_Parametrized
class Non_Parametrized:
    def __init__(self):
        self.name = "Test"
        self.age = 20


np = Non_Parametrized()
print(np.__dict__)


# Parametrized
class Parametrized:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Parametrized('Test', 21)
print(p.__dict__)
