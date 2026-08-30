# Given DataFrame as a dictionary


data = {
    "Math": [78, 82, 91, 65, 89],
    "Physics": [85, 79, 92, 88, 76],
    "Chemistry": [89, 94, 78, 88, 84],
    "Biology": [81, 85, 80, 77, 90]
}

# Write your code here




for key, value in data.items():
    value.sort()
    min_value=(min(value))
    max_value=(max(value))
    mean_value=(sum(value)/len(value))


    print(f'{key}: {min_value} - {max_value} - {mean_value}')

def quartile_calculate(data):
    for key, value in data.items():
        value.sort()
        median=0
        if len(value)%2==0:
            median=value[len(value)+1//2]
        else:
            median=value[len(value)//2]
    Ist_quartile=median

