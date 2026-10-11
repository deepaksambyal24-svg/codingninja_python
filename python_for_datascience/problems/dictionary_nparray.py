import numpy as np

# Dictionary - data
data = {
    "Temperature": 35,
    "Humidity": 75,
    "Pressure": 1013,
    "WindSpeed": 12
}

# Extracting keys and converting to a NumPy array
keys_array = np.array(data.keys())

print("Array of keys:", keys_array)