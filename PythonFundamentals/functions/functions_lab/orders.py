def get_price(product: str, quantity: int) -> str:
    prices = {
        "coffee": 1.5,
        "water": 1,
        "coke": 1.4,
        "snacks": 2,
    }
    price = prices[product] * quantity
    return f"{price:.2f}"


input_product = input()
product_quantity = int(input())
print(get_price(input_product, product_quantity))
