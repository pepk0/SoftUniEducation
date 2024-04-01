from abc import ABC, abstractmethod
from math import floor


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int,
                 budget: float) -> None:
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment: list = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not value.strip():
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, value) -> None:
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self) -> int:
        return self.__advantage

    @advantage.setter
    def advantage(self, value) -> None:
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self) -> None:
        pass

    def get_statistics(self) -> str:
        total_price_equipment = sum(x.price for x in self.equipment)

        if not self.equipment:
            avg_team_protection = 0
        else:
            avg_team_protection = sum(
                x.protection for x in self.equipment) // len(self.equipment)

        return (f"Name: {self.name}\nCountry: {self.country}\n"
                f"Advantage: {self.advantage} points\n"
                f"Budget: {self.budget:.2f}EUR\n"
                f"Wins: {self.wins}\n"
                f"Total Equipment Price: {total_price_equipment:.2f}\n"
                f"Average Protection: {int(avg_team_protection)}")
