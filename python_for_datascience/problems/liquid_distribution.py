# Input: Capacity of the container in liters
container_capacity = int(input())

# Input: Capacity of each bottle in liters
bottle_capacity = int(input())

# Your code goes here

print(f'Full bottles needed: {container_capacity // bottle_capacity}')
print(f'Remaining liquid: {container_capacity%bottle_capacity}')