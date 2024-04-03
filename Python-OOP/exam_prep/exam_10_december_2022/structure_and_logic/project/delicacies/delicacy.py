from abc import ABC, abstractmethod


class Delicacy(ABC):
    DELICACY_PORTION = 0

    def __init__(self, name: str, portion: int, price: float) -> None:
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not value.strip():
            raise ValueError("Name cannot be null or whitespace!")
        self.__name = value

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Price cannot be less or equal to zero!")
        self.__price = value

    @abstractmethod
    def details(self) -> str:
        pass
