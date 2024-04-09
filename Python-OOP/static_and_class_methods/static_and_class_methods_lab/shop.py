class Shop:
    def __init__(self, name: str, _type: str, capacity: int) -> None:
        self.name = name
        self.type = _type
        self.capacity = capacity
        self.items: dict = {}

    @classmethod
    def small_shop(cls, name: str, _type: str):
        return cls(name, _type, 10)

    def add_item(self, item_name: str) -> str:
        item_capacity = self.items.get(item_name, 0)

        if item_capacity == self.capacity:
            return "Not enough capacity in the shop"

        self.items[item_name] = item_capacity + 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name: str, amount: int) -> str:
        item_capacity = self.items.get(item_name, 0)

        if item_capacity == 0 or item_capacity < amount:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount

        if item_capacity == amount:
            self.items.pop(item_name)

        return f"{amount} {item_name} removed from the shop"

    def __repr__(self) -> str:
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


# fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
# small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
# print(fresh_shop)
# print(small_shop)
#
# print(fresh_shop.add_item("Bananas"))
# print(fresh_shop.remove_item("Tomatoes", 2))
#
# print(small_shop.add_item("Jeans"))
# print(small_shop.add_item("Jeans"))
# print(small_shop.remove_item("Jeans", 2))
# print(small_shop.items)
