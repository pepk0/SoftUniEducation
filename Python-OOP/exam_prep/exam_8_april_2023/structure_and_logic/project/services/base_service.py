from abc import ABC, abstractmethod


class BaseService(ABC):
    type_ = ""

    def __init__(self, name: str, capacity: int) -> None:
        self.name = name
        self.capacity = capacity
        self.robots: list = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not value.strip():
            raise ValueError("Service name cannot be empty!")
        self.__name = value

    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        if value <= 0:
            raise ValueError(
                "Service capacity cannot be less than or equal to 0!")
        self.__capacity = value

    @abstractmethod
    def details(self) -> str:
        pass
