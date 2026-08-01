# Given variables
store1_sales = {"Laptop": 15, "Smartphone": 30, "Tablet": 10, "Headphones": 20}
store2_sales = {"Smartphone": 50, "Tablet": 40, "Camera": 25, "Headphones": 30}

# Write your code here

for product, sales in store2_sales.items():
    if product in store1_sales:
        store1_sales[product] += sales
    else:
        store1_sales[product] = sales
print(f'Merged Sales Data: {store1_sales}')
print(f'Max Product: {max(store1_sales, key=store1_sales.get)} with Total Sales {max(store1_sales.values())}')