class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict) -> None:
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered: bool = False

    def add_extra(self, ingredient: str, quantity: int,
                  price_per_quantity: float):
        if self.ordered:
            return (f"Pizza {self.name} already prepared, "
                    f"and we can't make any changes!")

        elif ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity

        self.price += quantity * price_per_quantity

    def remove_ingredient(self, ingredient: str, quantity: int,
                          price_per_quantity: float):
        if self.ordered:
            return (f"Pizza {self.name} already prepared, "
                    f"and we can't make any changes!")

        elif ingredient not in self.ingredients:
            return (f"Wrong ingredient selected! "
                    f"We do not use {ingredient} in {self.name}!")

        elif self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"

        self.price -= quantity * price_per_quantity
        self.ingredients[ingredient] -= quantity

    def make_order(self) -> str:
        ingredients = ", ".join(
            f"{e}: {q}" for e, q in self.ingredients.items())
        if self.ordered:
            return (f"Pizza {self.name} already prepared, "
                    f"and we can't make any changes!")

        else:
            self.ordered = True
            return (f"You've ordered pizza {self.name} prepared with "
                    f"{ingredients} and the price will be {self.price}lv.")


# margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
# margarita.add_extra('mozzarella', 1, 0.5)
# margarita.add_extra('cheese', 1, 1)
# margarita.remove_ingredient('cheese', 1, 1)
# print(margarita.remove_ingredient('bacon', 1, 2.5))
# print(margarita.remove_ingredient('tomatoes', 2, 0.5))
# margarita.remove_ingredient('cheese', 2, 1)
# print(margarita.make_order())
# print(margarita.add_extra('cheese', 1, 1))
