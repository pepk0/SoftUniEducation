import re


def extract_name(text: str):
    name_pattern = r"(?:%)([A-Z]{1}[a-z]+)(?:%)"
    name = re.search(name_pattern, text)
    if name:
        return name.group(1)


def extract_product(text: str):
    name_pattern = r"(?:<)(\w+)(?:>)"
    name = re.search(name_pattern, text)
    if name:
        return name.group(1)


def extract_quantity(text: str):
    name_pattern = r"(?:\|)([0-9]+)(?:\|)"
    name = re.search(name_pattern, text)
    if name:
        return int(name.group(1))


def extract_price(text: str):
    name_pattern = r"([0-9]+[\.0-9]*)(?=\$)"
    name = re.search(name_pattern, text)
    if name:
        return float(name.group(1))


def validate_line(text: str):
    customer = extract_name(text)
    product = extract_product(text)
    quantity = extract_quantity(text)
    price = extract_price(text)
    if customer and product and quantity and price:
        total_per_customer = price * quantity
        return customer, product, total_per_customer


total_income = 0
while True:
    line_input = input()
    if line_input == "end of shift":
        break
    result = validate_line(line_input)
    if result:
        customer, product, total = result
        total_income += total
        print(f"{customer}: {product} - {total:.2f}")

print(f"Total income: {total_income:.2f}")
