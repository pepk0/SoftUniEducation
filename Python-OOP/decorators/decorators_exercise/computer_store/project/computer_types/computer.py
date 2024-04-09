from abc import ABC, abstractmethod


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str) -> None:
        self.model = model
        self.manufacturer = manufacturer
        self.processor = None
        self.ram = None
        self.price: int = 0

    @property
    def manufacturer(self) -> str:
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer: str) -> None:
        if not manufacturer.strip():
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = manufacturer

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, model: str) -> None:
        if not model.strip():
            raise ValueError("Model name cannot be empty.")

        self.__model = model

    @abstractmethod
    def configure_computer(self, processor: str, ram: int) -> str:
        ...

    def __repr__(self) -> str:
        return (f"{self.manufacturer} {self.model} with "
                f"{self.processor} and {self.ram}GB RAM")
