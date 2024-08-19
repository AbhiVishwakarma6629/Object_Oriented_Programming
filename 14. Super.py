class Computer:
    def __init__(self):
        print("Computer class constructor called...............!")
        self.ram = "8GB"
        self.storage = "512GB"

    def display(self):
        print(f"The specification is {self.ram} & {self.storage}")

class Mobile(Computer):
    def __init__(self):
        super().__init__()
        print("Mobile class constructor called..................!")
        self.version = "MEdiatek"


m1 = Mobile()
print(m1.__dict__)

