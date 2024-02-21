class Catalogue:
    def __init__(self, name: str, products: list = []) -> None:
        self.name = name
        self.products = products

    def add_product(self, product_name: str) -> None:
        self.products.append(product_name)

    def get_by_letter(self, letter: str) -> list:
        return [item for item in self.products if item[0] == letter]

    def __repr__(self) -> str:
        result = f"Items in the {self.name} catalogue:"
        for item in sorted(self.products):
            result += f"\n{item}"
        return result.strip()


# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)
