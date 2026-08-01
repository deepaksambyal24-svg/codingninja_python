from pyexpat.errors import codes

cars = [
    {"CarID": 1, "Fuel": "Petrol", "Engine": "Engine1"},
    {"CarID": 2, "Fuel": "Diesel", "Engine": "Engine2"},
    {"CarID": 3, "Fuel": "Petrol", "Engine": "Engine2"},
    {"CarID": 4, "Fuel": "Diesel", "Engine": "Engine1"},
    {"CarID": 5, "Fuel": "Electric", "Engine": "Engine3"},
    {"CarID": 6, "Fuel": "Hybrid", "Engine": "Engine3"},
]

# Write your code here
header=[]

for car in cars :
    car_type=car['Fuel'][0]+ car['Engine'][-1]
    header.append(car_type)
header.sort()
print("\t".join(["ID"] + header))

for car in cars :
    print(car['CarID'],end="\t")
    for code in header:
         if code==car['Fuel'][0]+ car['Engine'][-1]:
            print("1",end="\t")
         else:
             print("0",end="\t")
    print()