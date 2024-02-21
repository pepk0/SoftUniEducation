def make_dict(words: list) -> dict:
    return {words[i]: int(words[i + 1]) for i in range(0, len(words), 2)}


stock = make_dict(input().split())
products_to_search = [el for el in input().split()]

for product in products_to_search:
    result = f"Sorry, we don't have {product}"
    if product in stock:
        result = f"We have {stock[product]} of {product} left"
    print(result)
