from abc import ABC, abstractmethod


class Horse(ABC):
    MAX_SPEED: int = 0
    TRAIN_INCREMENT: int = 0

    def __init__(self, name: str, speed: int) -> None:
        self.name = name
        self.speed = speed
        self.is_taken: bool = False

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, value: int) -> None:
        if value > self.MAX_SPEED:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    @abstractmethod
    def train(self) -> None:
        pass
