# class methods are bounded to class not instances
# it belongs to class

class person:
    age =25
    @classmethod
    def print_age(cls):
        print(f"age is {cls.age}")   # becaouse it belongs to class so we are accessing it with class name person.class

# we don't need to create a class for this
person.print_age()
