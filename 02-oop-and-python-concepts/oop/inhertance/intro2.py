class vehicle:
    def start(self):
        print("start")
class car(vehicle):
    def getwheels(self):
        return 4
class bike(vehicle):
    def getwheels(self):
        return 3
car = car()
bike = bike()
print(f"car has{car.getwheels()} wheels")
print(f"bike has{bike.getwheels()} wheels")