def find_max_min(data):
    max_val = data[0]
    min_val = data[0]

    for i in data:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i

    return max_val, min_val