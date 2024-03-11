from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str, weight: float, food_eaten: int = 0) -> None:
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @staticmethod
    @abstractmethod
    def make_sound() -> str:
        pass

    @abstractmethod
    def feed(self, food) -> str or None:
        pass


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float,
                 food_eaten: int = 0) -> None:
        super().__init__(name, weight, food_eaten)
        self.wing_size = wing_size

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__} [{self.name}, {self.wing_size}, "
            f"{self.weight}, {self.food_eaten}]")


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str,
                 food_eaten: int = 0) -> None:
        super().__init__(name, weight, food_eaten)
        self.living_region = living_region

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__} [{self.name}, {self.weight}, "
                f"{self.living_region}, {self.food_eaten}]")
