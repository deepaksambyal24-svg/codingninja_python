import pandas as pd

data = {
    'Employee_ID': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    'Name': ['Aarav', 'Vivaan', 'Aditya', 'Vihaan', 'Arjun', 'Sai', 'Ishaan', 'Krishna', 'Anaya', 'Pooja'],
    'Age': [25, 30, 35, 40, 45, 28, 33, 38, 27, 32],
    'Department': ['HR', 'Finance', 'IT', 'IT', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
    'Salary': [50000, 60000, 70000, 80000, 75000, 65000, 70000, 72000, 68000, 75000]
}

# Write your code from here
df=pd.DataFrame(data)
print(df.head(2))
print(df.tail(3))