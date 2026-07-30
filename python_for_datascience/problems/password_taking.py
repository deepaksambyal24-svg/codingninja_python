import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
# Don't make changes to the above lines

# Write your code here
print('Enter a password (or END to stop).')
password = input()

if password != 'END' and len(password) <= 8:

    if str == 'END':
        print('END')

    if 'admin' in password:
        print(f'Invalid password {password} : contains \'admin\'')


    if " " in password:
        print(f"Invalid password '{password}': contains space")

print('END')


