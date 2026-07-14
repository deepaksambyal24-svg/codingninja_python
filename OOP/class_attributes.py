class vehicle:

    stopping_mechanism="brakes"   # attributes bound to class and shared by the all objects
    count=0
    def __init__(self,num_of_wheels)->None:
        self.num_of_wheels=num_of_wheels
        self.num_of_wheels=num_of_wheels

    def print_stopping_mechanism(self):
        print(vehicle.stopping_mechanism)
    def increment_count(self):
        vehicle.count+=1
    def get_count(self):
        return vehicle.count

car.print_stopping_mechanism()
car.increment_count()
print(car.get_count())
print(bicycle.get_count())
# to print an object in dictionary format
print(car.__dict__)
print(bicycle.__dict__)


car=vehicle(5)
truck=vehicle(6)
bicycle=vehicle(7)
print(car.num_of_wheels)
print(truck.num_of_wheels)
#variable which are not bound to object but bound to class are called attributes


