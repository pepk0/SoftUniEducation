import re


def find_items(text: str):
    pattern = r"^>>([A-Za-z]+)<<(\d+\.?\d*)!([0-9]+)$"
    result = re.search(pattern, text)
    if result:
        return result.group(1), float(result.group(2)), int(result.group(3))
    return None


total_price = 0
items = []
while True:
    item = input()
    if item == "Purchase":
        break
    item_info = find_items(item)
    if item_info:
        product, price, quantity = item_info
        total_price += price * quantity
        items.append(product)

print("Bought furniture:")
for item in items:  # didn't work with a unpack & spe=" "
    print(item)
print(f"Total money spend: {total_price:.2f}")
