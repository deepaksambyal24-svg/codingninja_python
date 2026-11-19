# Given data
food_items_per_day ={"monday": "Soya Chaap",
                     "tuesday": "Paneer",
                     "wednesday": "Bread & Milk",
                     "thursday" : "Fruits",
                     "friday": "Junk Food"}

# Write your code here
day=input().lower()
if day in food_items_per_day.keys():
    print(f'Food item for {day.title()} is {food_items_per_day.get(day)}.')

else :
    print(f'There is no such food item exists for {day.title()}.')
