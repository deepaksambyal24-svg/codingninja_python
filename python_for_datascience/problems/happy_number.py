# Given data
test_cases = [19, 2, 7, 23, 4, 16, 13]
# Don't make any changes to the test case above.


# Write your code here
for num in test_cases:
        current=num
        seen=[]
        while current not in seen:
            square_sum = 0
            for digit in str(current):
                 first=int(digit)**2
                 square_sum += first

            seen.append(current)
            current=square_sum


        if current == 1:
            print(f"Is {num} a happy number? True")
        else:
            print(f"Is {num} a happy number? False")



