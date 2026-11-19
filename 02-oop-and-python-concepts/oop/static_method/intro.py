#makes a function static in a class
class calculator:
    def sum(self,a,b):
        return a+b
calculator=calculator()     # To use the function we need to create a object
print(calculator.sum(3,4))

# in static method we donot need to create an object anymore


class calculator:
    @staticmethod
    def sum(a,b):
        return a+b
print(calculator.sum(3,4))