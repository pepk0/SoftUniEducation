from project.animals.animal import Mammal
from project.food import Fruit, Vegetable, Meat


class Mouse(Mammal):
    weight_per_food = 0.1

    def __init__(self, name: str, weight: float, living_region: str,
                 food_eaten: int = 0) -> None:
        super().__init__(name, weight, living_region, food_eaten)

    def make_sound(self) -> str:
        return "Squeak"

    def feed(self, food: Vegetable or Fruit) -> str or None:
        if not isinstance(food, (Vegetable, Fruit)):
            return (f"{self.__class__.__name__} does "
                    f"not eat {food.__class__.__name__}!")

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.weight_per_food


class Dog(Mammal):
    weight_per_food = 0.4

    def __init__(self, name: str, weight: float, living_region: str,
                 food_eaten: int = 0) -> None:
        super().__init__(name, weight, living_region, food_eaten)

    def make_sound(self) -> str:
        return "Woof!"

    def feed(self, food: Meat) -> str or None:
        if not isinstance(food, Meat):
            return (f"{self.__class__.__name__} does "
                    f"not eat {food.__class__.__name__}!")

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.weight_per_food


class Cat(Mammal):
    weight_per_food = 0.3

    def __init__(self, name: str, weight: float, living_region: str,
                 food_eaten: int = 0) -> None:
        super().__init__(name, weight, living_region, food_eaten)

    def make_sound(self) -> str:
        return "Meow"

    def feed(self, food: Meat or Vegetable) -> str or None:
        if not isinstance(food, (Meat, Vegetable)):
            return (f"{self.__class__.__name__} does "
                    f"not eat {food.__class__.__name__}!")

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.weight_per_food


class Tiger(Mammal):
    weight_per_food = 1

    def __init__(self, name: str, weight: float, living_region: str,
                 food_eaten: int = 0) -> None:
        super().__init__(name, weight, living_region, food_eaten)

    def make_sound(self) -> str:
        return "ROAR!!!"

    def feed(self, food: Meat) -> str or None:
        if not isinstance(food, Meat):
            return (f"{self.__class__.__name__} does "
                    f"not eat {food.__class__.__name__}!")

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.weight_per_food
