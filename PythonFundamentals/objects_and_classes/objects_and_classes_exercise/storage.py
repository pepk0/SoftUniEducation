class Storage:
    storage = []

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity

    def add_product(self, product: str) -> None:
        if len(Storage.storage) < self.capacity:
            Storage.storage.append(product)

    def get_products(self) -> list:
        return Storage.storage


# test cases for the above created class
# storage = Storage(4)
# storage.add_product("apple")
# storage.add_product("banana")
# storage.add_product("potato")
# storage.add_product("tomato")
# storage.add_product("bread")
# print(storage.get_products())
