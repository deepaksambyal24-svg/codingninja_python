# Define the function with custom exception
def validate_age(age):
    if age<0:
        raise ValueError('Age cannot be negative.')






# Don't change the below piece of code
try:
    age = int(input())
    validate_age(age)
    print("Age is valid.")
except ValueError as e:
    print(f"Error: {e}")

