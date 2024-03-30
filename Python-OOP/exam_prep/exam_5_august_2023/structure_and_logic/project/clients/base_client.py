from abc import ABC, abstractmethod


class BaseClient(ABC):
    def __init__(self, name: str, client_id: str, income: float,
                 interest: float) -> None:
        self.name = name
        self.client_id = client_id
        self.income = income
        self.interest = interest
        self.loans: list = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not value.strip():
            raise ValueError("Client name cannot be empty!")
        self.__name = value

    @property
    def client_id(self) -> str:
        return self.__client_id

    @client_id.setter
    def client_id(self, value) -> None:
        if len(value) != 10:
            raise ValueError("Client ID should be 10 symbols long!")
        self.__client_id = value

    @property
    def income(self) -> float:
        return self.__income

    @income.setter
    def income(self, value) -> None:
        if value <= 0:
            raise ValueError("Income must be greater than zero!")
        self.__income = value

    @abstractmethod
    def increase_clients_interest(self) -> None:
        pass
