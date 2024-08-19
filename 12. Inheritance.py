class Employee:
    bonus = 2000

    def display(self):
        print("This is employee class Method")


class Manager(Employee):
    bonus1 = 5000

    def show(self):
        print("This is a manager class")


e1 = Employee()
m1 = Manager()

e1.display()
m1.show()

print(m1.bonus)
print(e1.bonus1)


"""
Need of inheritane
->for Code-reusability (write once use many times)
-> When you have relations among classes
"""
