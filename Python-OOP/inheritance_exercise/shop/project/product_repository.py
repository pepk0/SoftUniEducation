from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: list = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        if product_name in self.products:
            return self.products[self.products.index(product_name)]

    def remove(self, product_name: str) -> None:
        if product_name in self.products:
            self.products.remove(product_name)

    def __repr__(self) -> str:
        return "\n".join(
            f'{product}: {product.quantity}' for product in self.products)
