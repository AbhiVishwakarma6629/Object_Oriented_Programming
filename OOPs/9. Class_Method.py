"""
-> Variable made for entire class (ALl Objects)
-> Only one copy is created and distributed to all objects
-> Modification in class variable impact on all objects

Class Methods
-> Method which works on class variables
-> First argument is class reference
-> Made using decorator @classmethod
"""

class Employee:
    company_name = "infosys"

    def __init__(self, nm, sal):
        self.name = nm
        self.salary = sal

    @classmethod
    def get_company_name(cls):
        print(f"company name is : {cls.company_name}")


e1 = Employee("Jay", 30000)
e2 = Employee("vijay", 50000)

Employee.company_name = "TCS"
print(Employee.company_name)
Employee.get_company_name()