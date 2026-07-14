# inheritance is hierachical of the classes
class Person:
    def print_person(self):
        print("person here")
class Employee(Person):             # in bracket write the name of class of inherited
    def print_employee(self):
        print("employee here")
emp = Employee()
emp.print_person()
