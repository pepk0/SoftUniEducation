product_stock = {}

while 1:
    command = input().split(": ")
    if command[0] == "statistics":
        break

    key, value = command[0], int(command[1])
    if key in product_stock:
        product_stock[key] += value
    else:
        product_stock[key] = value

print("Products in stock:")
for key, value in product_stock.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(product_stock)}")
print(f"Total Quantity: {sum(product_stock.values())}")
