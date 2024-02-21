class Inventory:
    def __init__(self, capacity: int, items: list = []) -> None:
        self.__capacity = capacity
        self.items = items

    def add_item(self, item: str) -> str | None:
        if len(self.items) < self.__capacity:
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self) -> int:
        return self.__capacity

    def __repr__(self) -> str:
        return (f"Items: {', '.join(self.items)}.\n"
                f"Capacity left: {self.__capacity - len(self.items)}")


# inventory = Inventory(2)
# inventory.add_item("potion")
# inventory.add_item("sword")
# print(inventory.add_item("bottle"))
# print(inventory.get_capacity())
# print(inventory)
