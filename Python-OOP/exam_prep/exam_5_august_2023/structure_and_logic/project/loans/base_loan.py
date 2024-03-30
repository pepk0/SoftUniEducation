from abc import ABC, abstractmethod


class BaseLoan(ABC):
    def __init__(self, interest_rate: float, amount: float) -> None:
        self.interest_rate = interest_rate
        self.amount = amount

    @abstractmethod
    def increase_interest_rate(self) -> None:
        pass
