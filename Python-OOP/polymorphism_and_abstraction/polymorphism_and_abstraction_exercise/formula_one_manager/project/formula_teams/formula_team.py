from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    min_budget: int = 1_000_000

    @abstractmethod
    def __init__(self, budget: int) -> None:
        self.budget = budget

    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, budget: int) -> None:
        if budget < self.min_budget:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = budget

    @abstractmethod
    def calculate_revenue_after_race(self, race_pos: int) -> int:
        pass
