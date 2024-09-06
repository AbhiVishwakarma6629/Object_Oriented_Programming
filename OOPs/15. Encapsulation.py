class Employee:
    def __init__(self):
        self.__finance = 10000 #Private Data
        self.__no_of_sales = 20 #Private Data

    def display(self):
        print(f"revenue is: {self.__finance} and the number of sales is {self.__no_of_sales}")
        obj.__finance = 20000
        print(f"revenue is: {self.__finance} and the number of sales is {self.__no_of_sales}")

class Hr:
    pass


obj = Employee()
ob1 = Hr()
obj.display()