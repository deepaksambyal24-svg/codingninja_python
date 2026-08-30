# Given DataFrame as a dictionary
data = {
    "ProductID": [101, 102, 103, None, 105],
    "Price": [9.99, 19.99, None, 29.99, 49.99],
    "Quantity": [1, 2, 3, None, None],
    "Category": ["A", "B", None, "C", "D"]
}

# Write your code here


for key, value in data.items():
    none_counter = 0
    data_type = ''
    for product in value:
        if product is None:
            none_counter += 1

        elif data_type == "":
            data_type = type(product)

    print(f'{key}: Data type = {str(data_type)}, None count = {none_counter}')

