class Father:
    def __init__(self):
        print("Father class constructor called.............!")
        self.Vehicle = "Scooter"

class Son(Father):
    # def __init__(self):
    #     print("Son class constructor called.................!")
    #     self.Vehicle = "BMW"
    pass

s = Son()
print(s.__dict__)