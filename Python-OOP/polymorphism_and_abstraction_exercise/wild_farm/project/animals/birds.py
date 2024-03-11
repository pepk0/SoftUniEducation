from project.animals.animal import Bird
from project.food import Meat, Food


class Owl(Bird):
    weight_per_food = 0.25
    food_animal_eats = (Meat,)

    def __init__(self, name: str, weight: float, wing_size: float,
                 food_eaten: int = 0) -> None:
        super().__init__(name, weight, wing_size, food_eaten)

    @staticmethod
    def make_sound() -> str:
        return "Hoot Hoot"

    def feed(self, food: Meat) -> str or None:
        if not isinstance(food, self.food_animal_eats):
            return (f"{self.__class__.__name__} does "
                    f"not eat {food.__class__.__name__}!")

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.weight_per_food


class Hen(Bird):
    weight_per_food = 0.35

    def __init__(self, name: str, weight: float, wing_size: float,
                 food_eaten: int = 0) -> None:
        super().__init__(name, weight, wing_size, food_eaten)

    @staticmethod
    def make_sound() -> str:
        return "Cluck"

    def feed(self, food: Food) -> str or None:
        self.food_eaten += food.quantity
        self.weight += food.quantity * self.weight_per_food
