class Veh:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def get_details(self):
        print("Name is: ",self.name)
        print("Color is: ", self.color)
        print("Price is: ", self.price)

    def max_speed(self):
        print("Maximum Speed is 100")

    def gear(self):
        print("Maximum gear is 5")

class Car(Veh):
    def max_speed(self):
        print("Maximum Speed is 150")

    def gear(self):
        print("Maximum gear is 6")

v1 = Veh("Ducati", "Red", 3600000)
c1 = Car("Supra", "White", "1.2cr")

v1.get_details()
v1.max_speed()
c1.get_details()
c1.max_speed()