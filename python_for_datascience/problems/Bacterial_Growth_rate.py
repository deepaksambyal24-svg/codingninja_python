# Input statements (given to the students)
initial_bacteria = 1000  # Initial number of bacteria
growth_rate = 1.1  # Growth rate per hour (10% increase means multiplying by 1.1 each hour)

# Input: Number of hours
number_Of_Hours=int(input())
# Calculate the final number of bacteria after the given number of hours
final_population=initial_bacteria*(growth_rate**number_Of_Hours)
# Print the number of bacteria after the given number of hours
print(f'Number of bacteria after {number_Of_Hours}: {int(final_population)}')
# Your code goes here
