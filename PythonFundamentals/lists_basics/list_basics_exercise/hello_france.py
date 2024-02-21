items = [el.split("->") for el in input().split("|")]
budget = int(input())

profit = 0
sold_items_total = 0
sold_items = []
ideal_price = {
    "Clothes": 50,
    "Shoes": 35,
    "Accessories": 20.5,
}

for item, price in items:
    price = float(price)
    price_limit = ideal_price[item]
    if price <= price_limit and price <= budget:
        budget -= price
        sold_item = price * 1.4
        sold_items_total += sold_item
        sold_items.append(f"{sold_item:.2f}")
        profit += (price * 1.4) - price

print(*sold_items, sep=" ")
print(f"Profit: {profit:.2f}")
if sold_items_total + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
